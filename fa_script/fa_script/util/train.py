from pathlib import Path
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript, SubScript
from fa_script.util.fairseq import FairseqTrainCommand

class TrainRunScript(RunScript):
    def __init__(self, expt_id, work_dir):
        self.expt_id = expt_id
        super().__init__(work_dir, use_localdir = True)

    def make_indices(self):
        indices = self.config['data_indices'][self.expt_id]
        return indices

    def make_copy(self, indices):
        for index in range(1, len(indices) + 1):
            self.append('mkdir -p ${{SGE_LOCALDIR}}/{}'.format(index))
        for n, index in enumerate(indices, start = 1):
            data_path = Path(self.config['data']).resolve() / str(index) / 'data-bin'
            self.append('cp -r {} ${{SGE_LOCALDIR}}/{} &'.format(data_path, n))
        self.append('wait')

    def make_data_bin_list(self, indices):
        data_bin_list = ['${{SGE_LOCALDIR}}/{}/data-bin'.format(n) for n in range(1, len(indices) + 1)]
        data_bin_list = ':'.join(data_bin_list)
        return data_bin_list

    def make_train_command(self, indices):
        command = FairseqTrainCommand(self.make_data_bin_list(indices), 'train')
        if 'restore_file' in self.config:
            command.restore_file(str(Path(self.config['restore_file'][self.expt_id]).resolve()))
        command.seed(self.config['seed_list'][self.expt_id])
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
        command.inverse_sqrt(self.config['train']['lr'], self.config['train']['warmup_updates'], self.config['train'].get('warmup_init_lr', 1.0e-07))
        command.clip_norm(self.config['train'].get('clip_norm', 1.0))
        command.weight_decay(self.config['train'].get('weight_decay', 1.0e-03))
        command.label_smoothed_cross_entropy(self.config['train'].get('label_smoothing', 0.1))
        return command

    def make(self):
        indices = self.make_indices()
        self.make_copy(indices)
        self.append('')
        self.append(str(self.make_train_command(indices)))

class TrainSubScript(SubScript):
    def __init__(self, mode):
        self.mode = mode
        super().__init__()

    def make(self):
        for n in range(len(self.config['seed_list'])):
            code_path = (Path(str(n)) / '{}.sh'.format(self.mode)).resolve()
            group = self.sub_config['group']
            h_rt = self.sub_config['train']['h_rt']
            node = self.sub_config['train'].get('node', 'rt_F')
            num_node = self.sub_config['train'].get('num_node', 1)
            p = self.sub_config['train'].get('p', None)
            var_dict = {'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, p = p, var_dict=var_dict)
            self.append(command)

