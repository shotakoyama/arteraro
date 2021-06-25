import yaml
from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.command import parallel_command, spm_command
from arteraro.auxt.util.load import load_config, check_sub_config
from arteraro.auxt.util.run import generate_run

class FixedErgPreprocessJobScript(JobScript):
    localdir = True

    def __init__(self, expt, trial, index):
        self.expt = expt
        self.trial = trial
        self.index = index
        super().__init__()

    def make_path(self):
        return '{}/{}/erg.sh'.format(self.trial, self.index)

    def make(self):
        j = self.config['threads']
        L = self.config['tokenization_lines']

        bpe_model = str(Path(self.config['bpe_model']).resolve())
        src_bpe_command = parallel_command(j, L,
                spm_command(bpe_model, dropout = self.config.get('src_dropout', None)))
        trg_bpe_command = parallel_command(j, L,
                spm_command(bpe_model, dropout = self.config.get('trg_dropout', None)))

        prepared_dir = Path(self.config['prepared'])
        source_path = (prepared_dir / str(self.expt) / str(self.index) / 'source.gz').resolve()
        target_path = (prepared_dir / str(self.expt) / str(self.index) / 'target.gz').resolve()

        self.append('zcat {} \\'.format(source_path))
        self.append('   | {} \\'.format(src_bpe_command))
        self.append('   > ${SGE_LOCALDIR}/src.txt &')
        self.append('zcat {} \\'.format(target_path))
        self.append('   | {} \\'.format(trg_bpe_command))
        self.append('   > ${SGE_LOCALDIR}/trg.txt &')
        self.append('wait')
        self.append('')

        min_len = self.config.get('min_len', 1)
        max_len = self.config['max_len']
        self.append('paste ${SGE_LOCALDIR}/src.txt ${SGE_LOCALDIR}/trg.txt \\')
        self.append('   | tondi --min-len {} --max-len {} \\'.format(min_len, max_len))
        self.append('   | progress \\')
        self.append('   | pigz -c \\')
        self.append('   > {}'.format(Path('{}/{}/train.gz'.format(self.trial, self.index)).resolve()))

class FixedErgPreprocessRunScript(RunScript):
    def make_path(self):
        return 'preproc.sh'

class FixedErgPreprocessSubScript(SubScript):
    def __init__(self, group, script_list):
        self.group = group
        super().__init__(script_list)

    def make_path(self):
        return 'preproc.{}.sh'.format(self.group)

    def make_h_rt(self):
        return self.sub_config['h_rt']

    def make_node(self):
        return self.sub_config.get('node', 'rt_C.large')

def get_num_groups():
    config = load_config()
    return config['groups']

def run(script_list):
    run_script = FixedErgPreprocessRunScript(script_list)

def sub(script_list):
    num_groups = get_num_groups()
    width = (len(script_list) - 1) // num_groups + 1
    for group in range(num_groups):
        script_sub_list = script_list[group * width : (group + 1) * width]
        sub_script = FixedErgPreprocessSubScript(group, script_sub_list)

def fix_preproc():
    config = load_config()
    num_expts = config['expt']
    num_iters = config['iter']
    num_indices = config['indices']

    script_list = []
    for expt in range(num_expts):
        for i in range(num_iters):
            trial = expt * num_iters + i
            for index in range(num_indices):
                script = FixedErgPreprocessJobScript(expt, trial, index)
                script_list.append(script)

    if check_sub_config():
        sub(script_list)
    else:
        run(script_list)

