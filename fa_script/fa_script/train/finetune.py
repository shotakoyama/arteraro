from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config
from fa_script.util.spm import spm_command
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript, SubScript
from fa_script.util.fairseq import FairseqTrainCommand

class FinetuneTrainRunScript(RunScript):
    def __init__(self, config, n):
        self.n = n
        super().__init__(config, use_localdir=True)

    def make(self):
        indices = self.config['data_indices'][self.n]
        for n in range(1, len(indices) + 1):
            self.append('mkdir -p ${{SGE_LOCALDIR}}/{}'.format(n))
        for n, index in enumerate(indices, start = 1):
            data_path = Path(self.config['data']).resolve() / str(index) / 'data-bin'
            self.append('cp -r {} ${{SGE_LOCALDIR}}/{}'.format(data_path, n))
        data_bin_list = ['${{SGE_LOCALDIR}}/{}/data-bin'.format(n) for n in range(1, len(indices) + 1)]
        data_bin_list = ':'.join(data_bin_list)

        self.append('')

        command = FairseqTrainCommand(data_bin_list, 'train')
        if 'restore_file' in self.config:
            command.restore_file(self.config['restore_file'][self.n])
        command.seed(self.config['seed_list'][self.n])
        command.log()
        command.fp16()
        if self.config.get('no_c10d', False):
            command.no_c10d()
        command.epoch(self.config['train']['max_epoch'])
        command.batch(self.config['train']['update_freq'], self.config['train']['max_tokens'])
        command.arch(
                prenorm = self.config['train'].get('prenorm', True),
                arch = self.config['train'].get('arch', 'big'),
                share_all_embeddings = self.config['train'].get('share_all_embeddings', True),
                dropout = self.config['train'].get('dropout', 0.3),
                attention_dropout = self.config['train'].get('attention_dropout', 0.2),
                activation_dropout = self.config['train'].get('activation_dropout', 0.2),
                activation_fn = self.config['train'].get('activation_fn', 'gelu'))
        command.adam(*self.config['train'].get('adam_betas', [0.9, 0.999]))
        command.inverse_sqrt(self.config['train']['lr'], self.config['train']['warmup_updates'], self.config['train']['warmup_init_lr'])
        if 'clip_norm' in self.config:
            command.clip_norm(self.config['train']['clip_norm'])
        if 'weight_decay' in self.config:
            command.weight_decay(self.config['train']['weight_decay'])
        command.label_smoothed_cross_entropy(self.config['train']['label_smoothing'])
        self.append(str(command))

class FinetuneTrainSubScript(SubScript):
    def make(self):
        for n in range(len(self.config['seed_list'])):
            code_path = (Path(str(n)) / 'expt.sh').resolve()
            group = self.sub_config['group']
            h_rt = self.sub_config['train']['h_rt']
            node = self.sub_config['train'].get('node', 'rt_F')
            num_node = self.sub_config['train'].get('num_node', 1)
            workdir = '"${{BASEDIR}}/{}"'.format(n)
            var_dict = {'WORKDIR': workdir, 'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, var_dict=var_dict)
            self.append(command)


def main():
    config = load_config()
    seed_list = config['seed_list']
    for n in range(len(seed_list)):
        Path(str(n)).mkdir(exist_ok=True)
        script = FinetuneTrainRunScript(config, n)
        with open(Path(str(n)) / 'train.sh', 'w') as f:
            print(script, file = f)

    if check_sub_config():
        sub_config = load_sub_config()
        sub_script = FinetuneTrainSubScript(config, sub_config)
        with open('train.sh', 'w') as f:
            print(sub_script, file=f)

