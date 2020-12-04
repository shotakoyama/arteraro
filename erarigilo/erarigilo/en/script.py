from argparse import ArgumentParser
from pathlib import Path
from .util.script_util import *
import yaml

class NoiserRunScript(Script):
    def __init__(self, config, n):
        self.n = n
        super().__init__(config)
        self.make_config()

    def header(self):
        self.append('set -ex')
        if self.config.get('mode', None) == 'abci':
            self.append('. /etc/profile.d/modules.sh')
        self.append('') # 空行
        cwd = Path.cwd().resolve()
        self.dir_path = cwd / str(self.n)
        self.append(f'cd {self.dir_path}')
        if 'source_path' in self.config:
            env = self.config['source_path']
            self.append(f'. {env}')
        self.append('') # 空行

    def spm_command(self, dropout = None):
        spm_model = self.config['spm_model']
        if dropout is None:
            command = f'pyspm_encode --model_file {spm_model}'
        else:
            command = f'pyspm_encode --model_file {spm_model} --dropout {dropout}'
        return command

    def make(self):
        self.append('mkdir ${SGE_LOCALDIR}/tmp')
        self.append('TMPDIR=${SGE_LOCALDIR}/tmp')

        # noise
        lines = self.config['lines']
        threads = self.config['threads']
        preprocessed = self.config['preprocessed']
        self.append(f'zcat {preprocessed} \\')
        if 'corpus_size' in self.config:
            corpus_size = self.config['corpus_size']
            self.append(f'\t| head -n {corpus_size} \\')
        self.append(f'\t| parallel --pipe -j {threads} -k --L {lines} "OMP_NUM_THREADS=1 en_erg_noise" \\')
        self.append(f'\t| progress > ${{SGE_LOCALDIR}}/noised.txt')

        # form
        form_lines = self.config.get('form_lines', lines)
        self.append('cat ${SGE_LOCALDIR}/noised.txt \\')
        self.append(f'\t| parallel --pipe -j {threads} -k --L {form_lines} en_erg_form \\')
        self.append(f'\t| progress > ${{SGE_LOCALDIR}}/formed.txt')
        self.append(f'rm ${{SGE_LOCALDIR}}/noised.txt')

        # tokenize
        tokenize_lines = self.config.get('tokenize_lines', lines)
        src_dropout = self.config.get('src_dropout', None)
        trg_dropout = self.config.get('trg_dropout', None)
        src_spm_command = self.spm_command(src_dropout)
        trg_spm_command = self.spm_command(trg_dropout)
        self.append(f'cat ${{SGE_LOCALDIR}}/formed.txt | cut -f 1 | parallel --pipe -j {threads} -k --L {tokenize_lines} "{src_spm_command}" > ${{SGE_LOCALDIR}}/src.txt &')
        self.append(f'cat ${{SGE_LOCALDIR}}/formed.txt | cut -f 2 | parallel --pipe -j {threads} -k --L {tokenize_lines} "{trg_spm_command}" > ${{SGE_LOCALDIR}}/trg.txt &')
        self.append('wait')
        min_len = self.config['min_len']
        max_len = self.config['max_len']
        self.append(f'erg_paste ${{SGE_LOCALDIR}}/src.txt ${{SGE_LOCALDIR}}/trg.txt --min-len {min_len} --max-len {max_len} | progress | pigz -c > train.gz')

    def make_config(self):
        with open(self.dir_path / 'config.yaml', 'w') as f:
            dct = {'noiser' : self.config['noiser']}
            print(yaml.safe_dump(dct), file = f)


class NoiserSubScript(SubScript):
    def make(self):
        group = self.config['group']
        trials = self.config['trials']
        for n in range(trials):
            command = f'{n}/run.sh'
            h_rt = self.config['h_rt']
            self.add(command, group, h_rt)


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', dest = 'config', default = 'config.yaml')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    trials = config['trials']
    cwd = Path.cwd()
    for n in range(trials):
        path = cwd / str(n)
        path.mkdir(exist_ok = True, parents = True)
        run_script = NoiserRunScript(config, n)
        with open(path / 'run.sh', 'w') as f:
            print(str(run_script), file = f)

    sub_script = NoiserSubScript(config)
    with open('sub.sh', 'w') as f:
        print(str(sub_script), file = f)

