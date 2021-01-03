from pathlib import Path
from fa_script.util.load import load_config, check_sub_config, load_config_and_sub_config
from fa_script.util.spm import spm_command
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript
from fa_script.util.data import DataSubScript
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
    def __init__(self, work_dir, n, first_index):
        self.n = n
        self.first_index = first_index
        super().__init__(work_dir, use_localdir = True)

    def make_prepare(self, src, trg):
        self += [
            'echo -n > {}'.format(src),
            'echo -n > {}'.format(trg)]
        model = self.config['bpe']['model']
        src_p = self.config['bpe'].get('src_dropout', None)
        trg_p = self.config['bpe'].get('trg_dropout', None)
        for mode in ['m2', 'tsv']:
            if mode in self.config['dataset']:
                self += command_list(
                        mode,
                        self.config['dataset'][mode],
                        self.config['dataset'].get('{}_sample'.format(mode), None),
                        model, src_p, trg_p, src, trg)

    def make_src_dict_path(self):
        if (self.first_index is not None) and (self.n != self.first_index):
            src_dict_path = '{}/data-bin/dict.src.txt'.format(self.first_index)
        else:
            src_dict_path = self.config.get('src_dict_path', None)
        if src_dict_path is not None:
            src_dict_path = str(Path(src_dict_path).resolve())
        return src_dict_path

    def make(self):
        src = '${SGE_LOCALDIR}/train.src'
        trg = '${SGE_LOCALDIR}/train.trg'
        self.make_prepare(src, trg)
        train_pref = '${SGE_LOCALDIR}/train'
        valid_pref = str(Path(self.config['dataset']['valid_pref']).resolve())
        dest_dir = 'data-bin'
        src_dict_path = self.make_src_dict_path()
        self.append(fairseq_preprocess_command(train_pref, valid_pref, dest_dir, src_dict_path))

def run():
    config = load_config()
    if 'src_dict_path' in config:
        first_trial = None
    else:
        first_trial = config.get('first_trial', 0)
    for n in range(config['trial']):
        base_dir = Path(str(n)).resolve()
        base_dir.mkdir(exist_ok = True)
        script = FinetuneDataRunScript(base_dir, n, first_trial)
        with open(base_dir / 'data.sh', 'w') as f:
            f.write(str(script))
    return first_trial

def sub(first_trial):
    config, sub_config = load_config_and_sub_config()
    indices = [n for n in range(config['trial'])]
    if first_trial is not None:
        indices = [n for n in indices if n != first_trial]
        sub_script = DataSubScript([first_trial])
        with open('first_sub.sh', 'w') as f:
            f.write(str(sub_script))
    sub_script = DataSubScript(indices)
    with open('sub.sh', 'w') as f:
        f.write(str(sub_script))

def main():
    first_trial = run()
    if check_sub_config():
        sub(first_trial)

