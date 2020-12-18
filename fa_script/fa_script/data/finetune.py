from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config
from fa_script.util.spm import spm_command
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript, SubScript
from fa_script.util.fairseq import fairseq_preprocess_command

def command_list_templete(mode):
    if mode == 'm2':
        src_command = 'cat {} | m2_to_src | reguligilo -a | {} >> {}'
        trg_command = 'cat {} | m2_to_trg | reguligilo -a | {} >> {}'
    elif mode == 'tsv':
        src_command = 'cut -f 1 {} | reguligilo -a | {} >> {}'
        trg_command = 'cut -f 2 {} | reguligilo -a | {} >> {}'
    else:
        assert False
    return src_command, trg_command

def command_list(mode, corpora, sample, spm_model, src_dropout, trg_dropout, src, trg):
    if sample is None:
        sample = [1] * len(corpora)
    assert len(corpora) == len(sample)
    path_list = [
            str(Path(corpus).resolve())
            for repeat, corpus in zip(sample, corpora)
            for _ in range(repeat)]
    path_list = ' '.join(path_list)
    src_command, trg_command = command_list_templete(mode)
    src_subword_command = spm_command(Path(spm_model).resolve(), src_dropout)
    trg_subword_command = spm_command(Path(spm_model).resolve(), trg_dropout)
    command_list = [
            src_command.format(path_list, src_subword_command, src),
            trg_command.format(path_list, trg_subword_command, trg)]
    return command_list

class FinetuneDataRunScript(RunScript):
    def __init__(self, config, n, first_index):
        self.n = n
        self.first_index = first_index
        super().__init__(config, use_localdir = True)

    def make_prepare(self, src, trg):
        self += [
            'echo -n > {}'.format(src),
            'echo -n > {}'.format(trg)]
        model = self.config['bpe']['model']
        src_p = self.config['bpe'].get('src_dropout', None)
        trg_p = self.config['bpe'].get('trg_dropout', None)
        if 'm2' in self.config['dataset']:
            self += command_list(
                    'm2',
                    self.config['dataset']['m2'],
                    self.config['dataset'].get('m2_sample', None),
                    model, src_p, trg_p, src, trg)
        if 'tsv' in self.config['dataset']:
            self += command_list(
                    'tsv',
                    self.config['dataset']['tsv'],
                    self.config['dataset'].get('tsv_sample', None),
                    model, src_p, trg_p, src, trg)

    def make(self):
        src = '${SGE_LOCALDIR}/train.src'
        trg = '${SGE_LOCALDIR}/train.trg'
        self.make_prepare(src, trg)
        train_pref = '${SGE_LOCALDIR}/train'
        valid_pref = self.config['dataset']['valid_pref']
        valid_pref = str(Path(valid_pref).resolve())
        dest_dir = 'data-bin'
        if (self.first_index is not None) and (self.n != self.first_index):
            src_dict_path = '{}/data-bin/dict.src.txt'.format(self.first_index)
            src_dict_path = str(Path(src_dict_path).resolve())
        else:
            src_dict_path = self.config.get('src_dict_path',  None)
        preprocess_command = fairseq_preprocess_command(train_pref, valid_pref, dest_dir, src_dict_path)
        self.append(preprocess_command)

class FinetuneDataSubScript(SubScript):
    def __init__(self, config, sub_config, indices):
        self.indices = indices
        super().__init__(config, sub_config)

    def make(self):
        for n in self.indices:
            code_path = (Path(str(n)) / 'data.sh').resolve()
            group = self.sub_config['group']
            h_rt = self.sub_config['h_rt']
            node = self.sub_config.get('node', 'rt_C.large')
            num_node = self.sub_config.get('num_node', 1)
            workdir = '"${{BASEDIR}}/{}"'.format(n)
            var_dict = {'WORKDIR': workdir, 'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, var_dict=var_dict)
            self.append(command)

def main():
    config = load_config()
    if 'src_dict_path' in config:
        first_trial = None
    else:
        first_trial = config.get('first_trial', 0)
    for n in range(config['trial']):
        Path(str(n)).mkdir(exist_ok=True)
        script = FinetuneDataRunScript(config, n, first_trial)
        with open(Path(str(n)) / 'data.sh', 'w') as f:
            print(script, file = f)

    if check_sub_config():
        sub_config = load_sub_config()
        indices = [n for n in range(config['trial'])]
        if first_trial is not None:
            indices = [n for n in indices if n != first_trial]
            sub_script = FinetuneDataSubScript(config, sub_config, [first_trial])
            with open('first_sub.sh', 'w') as f:
                print(sub_script, file = f)

        sub_script = FinetuneDataSubScript(config, sub_config, indices)
        with open('sub.sh', 'w') as f:
            print(sub_script, file = f)

