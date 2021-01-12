from pathlib import Path
from fa_script.util.load import load_config, load_config_and_sub_config, check_sub_config
from fa_script.util.spm import spm_command
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript
from fa_script.util.data import DataSubScript
from fa_script.util.fairseq import fairseq_preprocess_command

class PretrainDataRunScript(RunScript):
    def __init__(self, work_dir, n, first_index):
        self.n = n
        self.first_index = first_index
        super().__init__(work_dir, use_localdir = True)

    def make_src_dict_path(self):
        if (self.first_index is not None) and (self.n != self.first_index):
            src_dict_path = '{}/data-bin/dict.src.txt'.format(self.first_index)
        else:
            src_dict_path = self.config.get('src_dict_path', None)
        if src_dict_path is not None:
            src_dict_path = str(Path(src_dict_path).resolve())
        return src_dict_path

    def make(self):
        if 'base_dir' in self.config['pretrain']:
            train_gzip = Path(self.config['pretrain']['base_dir']).resolve() / str(self.n) / 'train.gz'
        else:
            train_gzip = ' '.join([str(Path(x).resolve() / str(self.n) / 'train.gz') for x in self.config['pretrain']['base_list']])
        self.append('zcat {} | cut -f 1 > ${{SGE_LOCALDIR}}/train.src &'.format(train_gzip))
        self.append('zcat {} | cut -f 2 > ${{SGE_LOCALDIR}}/train.trg &'.format(train_gzip))
        self.append('wait')
        train_pref = '${SGE_LOCALDIR}/train'
        valid_pref = str(Path(self.config['dataset']['valid_pref']).resolve())
        dest_dir = 'data-bin'
        src_dict_path = self.make_src_dict_path()
        command = fairseq_preprocess_command(train_pref, valid_pref, dest_dir, src_dict_path)
        self.append(command)

def run():
    config = load_config()
    first_trial = 0
    for n in range(config['pretrain']['trials']):
        base_dir = Path(str(n)).resolve()
        base_dir.mkdir(exist_ok = True)
        script = PretrainDataRunScript(base_dir, n, first_trial)
        with open(base_dir / 'data.sh', 'w') as f:
            f.write(str(script))
    return first_trial

def sub(first_trial):
    config = load_config()
    indices = [n for n in range(config['pretrain']['trials'])]
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

