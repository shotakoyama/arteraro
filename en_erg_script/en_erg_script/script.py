from pathlib import Path
from .util import *
import yaml

class NoiserRunScript(RunScript):
    def __init__(self, n, config):
        self.n = n
        self.cwd = Path.cwd().resolve()
        with open('config.yaml') as f:
            self.noise_list = yaml.safe_load(f)
        super().__init__(config)

    def write(self):
        (self.cwd / str(self.n)).mkdir(exist_ok = True, parents = True)
        with open(self.cwd / str(self.n) / 'aeg.sh', 'w') as f:
            print(str(self), file = f)

    def make_copy(self):
        for i in range(len(self.noise_list)):
            for name, dct in self.noise_list[i].items():
                for key, value in dct.items():
                    if key.endswith('path'):
                        value = str(Path(value).resolve())
                        target = '${{SGE_LOCALDIR}}/{}'.format(Path(value).name)
                        self.append('cp {} "{}"'.format(value, target))
                        self.noise_list[i][name][key] = target
        with open(self.cwd / str(self.n) / 'config.yaml', 'w') as f:
            print(yaml.safe_dump(self.noise_list), file = f)

    def make_noise(self):
        self.append('zcat {} \\'.format(' '.join([str(Path(x).resolve()) for x in self.config['preprocessed_gzip_list']])))
        if 'corpus_size' in self.config:
            self.append('   | head -n {} \\'.format(self.config['corpus_size']))
        self.append('   | parallel --pipe -j {} -k --L {} "OMP_NUM_THREADS=1 en_erg_noise" \\'.format(
            self.config['threads'], self.config['lines']))
        self.append('   | progress > ${SGE_LOCALDIR}/noised.txt')

    def make_form(self):
        self.append('cat ${SGE_LOCALDIR}/noised.txt \\')
        self.append('   | parallel --pipe -j {} -k --L {} en_erg_form \\'.format(
            self.config['threads'], self.config.get('forming_lines', self.config['lines'])))
        self.append('   | progress > ${SGE_LOCALDIR}/formed.txt')
        self.append('rm ${SGE_LOCALDIR}/noised.txt')

    def make_tokenize(self):
        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 1 \\')
        self.append('   | parallel --pipe -j {} -k --L {} "{}" > ${{SGE_LOCALDIR}}/src.txt &'.format(
            self.config['threads'], self.config.get('tokenization_lines', self.config['lines']),
            spm_command(self.config['spm_model'], self.config.get('src_dropout', None))))
        self.append('cat ${SGE_LOCALDIR}/formed.txt \\')
        self.append('   | cut -f 2 \\')
        self.append('   | parallel --pipe -j {} -k --L {} "{}" > ${{SGE_LOCALDIR}}/trg.txt &'.format(
            self.config['threads'], self.config.get('tokenization_lines', self.config['lines']),
            spm_command(self.config['spm_model'], self.config.get('trg_dropout', None))))
        self.append('wait')

    def make(self):
        self.make_copy()
        self.append('')
        self.make_noise()
        self.append('')
        self.make_form()
        self.append('')
        self.make_tokenize()
        self.append('')
        self.append('erg_paste ${{SGE_LOCALDIR}}/src.txt ${{SGE_LOCALDIR}}/trg.txt --min-len {} --max-len {} \\'.format(
            self.config['min_len'], self.config['max_len']))
        self.append('   | progress | pigz -c > train.gz')


class NoiserSubScript(SubScript):
    def __init__(self, trials, config):
        self.trials = trials
        super().__init__(config)

    def write(self):
        with open(Path.cwd().resolve() / 'sub.sh', 'w') as f:
            print(str(self), file = f)

    def make(self):
        for n in range(self.trials):
            self.append(qsub_command(
                f'{n}/aeg.sh',
                self.config.get('group', None),
                self.config['h_rt'],
                self.config.get('node', 'rt_C.large'),
                self.config.get('num_node', 1),
                {'WORKDIR': '"${{BASEDIR}}/{}"'.format(n), 'SGE_QSUB': 'yes'}))


def main():
    with open('aeg_config.yaml') as f:
        aeg_config = yaml.safe_load(f)

    trials = aeg_config['trials']
    cwd = Path.cwd()
    for n in range(trials):
        run_script = NoiserRunScript(n, aeg_config)
        run_script.write()

    if Path('sub_config.yaml').exists():
        with open('sub_config.yaml') as f:
            sub_config = yaml.safe_load(f)
        sub_script = NoiserSubScript(trials, sub_config)
        sub_script.write()

