import yaml
from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.command import parallel_command
from arteraro.auxt.util.load import load_config, check_sub_config

class FixedErgPrepareJobScript(JobScript):
    localdir = True

    def __init__(self, expt, index):
        self.expt = expt
        self.index = index
        with open('config.yaml') as f:
            self.aeg_rules = yaml.safe_load(f)
        if self.aeg_rules is None:
            self.aeg_rules = []
        super().__init__()

    def make_path(self):
        return '{}/{}/erg.sh'.format(self.expt, self.index)

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
        dir_path = Path('{}/{}'.format(self.expt, self.index))
        dir_path.mkdir(exist_ok = True, parents=True)
        with open(dir_path / 'config.yaml', 'w') as f:
            print(yaml.safe_dump(self.aeg_rules), file = f)

    def make_erg(self):
        input_path = str(Path(self.config['readied'][self.index]).resolve())
        j = self.config['threads']
        L = self.config['lines']
        ratio = self.config['ratio']
        command = 'OMP_NUM_THREADS=1 erg run en --ratio {}'.format(ratio)
        if 'languages' in self.config:
            languages = ':'.join(self.config['languages'])
            command += ' --languages {}'.format(languages)
        command = '"{}"'.format(command)
        command = parallel_command(j, L, command)
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
        self.append('   | progress > ${SGE_LOCALDIR}/formed.txt')
        self.append('')

    def make(self):
        if check_sub_config():
            self.make_copy()
        self.make_config()
        self.make_erg()
        self.make_form()

        source_path = Path('{}/{}/source.gz'.format(self.expt, self.index)).resolve()
        target_path = Path('{}/{}/target.gz'.format(self.expt, self.index)).resolve()
        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 1 \\')
        self.append('   | pigz -c \\')
        self.append('   > {} &'.format(source_path))

        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 2 \\')
        self.append('   | pigz -c \\')
        self.append('   > {} &'.format(target_path))

        self.append('wait')

class FixedErgPrepareRunScript(RunScript):
    def make_path(self):
        return 'prepare.sh'

class FixedErgPrepareSubScript(SubScript):
    def __init__(self, group, script_list):
        self.group = group
        super().__init__(script_list)

    def make_path(self):
        return 'prepare.{}.sh'.format(self.group)

    def make_h_rt(self):
        return self.sub_config['h_rt']

    def make_node(self):
        return self.sub_config.get('node', 'rt_C.large')

def get_num_groups():
    config = load_config()
    return config['groups']

def run(script_list):
    run_script = FixedErgPrepareRunScript(script_list)

def sub(script_list):
    num_groups = get_num_groups()
    width = (len(script_list) - 1) // num_groups + 1
    for group in range(num_groups):
        script_sub_list = script_list[group * width : (group + 1) * width]
        sub_script = FixedErgPrepareSubScript(group, script_sub_list)

def fix_prepare():
    config = load_config()
    num_expts = config['expt']
    num_indices = len(config['readied'])

    script_list = [FixedErgPrepareJobScript(expt, index)
            for expt in range(num_expts)
            for index in range(num_indices)]

    if check_sub_config():
        sub(script_list)
    else:
        run(script_list)

