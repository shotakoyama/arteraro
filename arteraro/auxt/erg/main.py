import yaml
from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.command import parallel_command, spm_command
from arteraro.auxt.util.load import load_config, check_sub_config
from arteraro.auxt.util.run import generate_run

class ErgJobScript(JobScript):
    localdir = True

    def __init__(self, trial, index):
        self.trial = trial
        self.index = index
        with open('config.yaml') as f:
            self.aeg_rules = yaml.safe_load(f)
        super().__init__()

    def make_path(self):
        return '{}/{}/erg.sh'.format(self.trial, self.index)

    def make_copy(self):
        for i, rule in enumerate(self.aeg_rules):
            for name, dct in rule.items(): # num of iterations of this loop is 1
                for key, value in dct.items():
                    if key.endswith('path'):
                        value = Path(value).resolve()
                        target = '${{SGE_LOCALDIR}}/{}'.format(value.name)
                        self.append('cp {} "{}"'.format(str(value), target))
                        self.aeg_rules[i][name][key] = target
        self.append('')

    def make_config(self):
        dir_path = Path('{}/{}'.format(self.trial, self.index))
        dir_path.mkdir(exist_ok = True, parents=True)
        with open(dir_path / 'config.yaml', 'w') as f:
            print(yaml.safe_dump(self.aeg_rules), file = f)

    def make_erg(self):
        input_path = str(Path(self.config['readied'][self.index]).resolve())
        j = self.config['threads']
        L = self.config['lines']
        ratio = self.config['ratio']
        languages = ':'.join(self.config['languages'])
        command = parallel_command(j, L, '"OMP_NUM_THREADS=1 erg run en --ratio {} --languages {}"'.format(ratio, languages))
        self.append('zcat {} \\'.format(input_path))
        self.append('   | {} \\'.format(command))
        self.append('   | progress > ${SGE_LOCALDIR}/generated.txt')
        self.append('')

    def make_form(self):
        j = self.config['threads']
        L = self.config['forming_lines']
        command = parallel_command(j, L, '"erg form en"')
        self.append('cat ${SGE_LOCALDIR}/generated.txt \\')
        self.append('   | {} \\'.format(command))
        self.append('   | progress \\')
        self.append('   > ${SGE_LOCALDIR}/formed.txt')
        self.append('')

    def make_bpe(self):
        j = self.config['threads']
        L = self.config['tokenization_lines']
        bpe_model = str(Path(self.config['bpe_model']).resolve())
        src_bpe_command = parallel_command(j, L,
                spm_command(bpe_model, dropout = self.config.get('src_dropout', None)))
        trg_bpe_command = parallel_command(j, L,
                spm_command(bpe_model, dropout = self.config.get('trg_dropout', None)))
        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 1 \\')
        self.append('   | {} \\'.format(src_bpe_command))
        self.append('   > ${SGE_LOCALDIR}/src.txt &')
        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 2 \\')
        self.append('   | {} \\'.format(trg_bpe_command))
        self.append('   > ${SGE_LOCALDIR}/trg.txt &')
        self.append('wait')
        self.append('')

    def make(self):
        if check_sub_config():
            self.make_copy()
        self.make_config()
        self.make_erg()
        self.make_form()
        self.make_bpe()

        min_len = self.config.get('min_len', 1)
        max_len = self.config['max_len']
        self.append('paste ${SGE_LOCALDIR}/src.txt ${SGE_LOCALDIR}/trg.txt \\')
        self.append('   | tondi --min-len {} --max-len {} \\'.format(min_len, max_len))
        self.append('   | progress \\')
        self.append('   | pigz -c \\')
        self.append('   > {}'.format(Path('{}/{}/train.gz'.format(self.trial, self.index)).resolve()))

class ErgRunScript(RunScript):
    def make_path(self):
        return 'run.sh'

class ErgSubScript(SubScript):
    def __init__(self, group, script_list):
        self.group = group
        super().__init__(script_list)

    def make_path(self):
        return 'sub.{}.sh'.format(self.group)

    def make_h_rt(self):
        return self.sub_config['h_rt']

    def make_node(self):
        return self.sub_config.get('node', 'rt_C.large')

def run_erg(script_list):
    run_script = ErgRunScript(script_list)

def get_num_groups():
    config = load_config()
    return config['groups']

def sub_erg(script_list):
    num_groups = get_num_groups()
    width = (len(script_list) - 1) // num_groups + 1
    for group in range(num_groups):
        script_sub_list = script_list[group * width : (group + 1) * width]
        sub_script = ErgSubScript(group, script_sub_list)

def erg():
    config = load_config()
    num_trials = config['trials']
    num_indices = len(config['readied'])

    script_list = [ErgJobScript(trial, index)
            for trial in range(num_trials)
            for index in range(num_indices)]

    if check_sub_config():
        sub_erg(script_list)
    else:
        run_erg(script_list)

