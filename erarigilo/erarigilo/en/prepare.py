from argparse import ArgumentParser
from pathlib import Path
from .util.script_util import *
import yaml

class PrepareRunScript(RunScript):
    def make(self):
        lines = self.config['lines']
        threads = self.config.get('threads', 40)
        input_files = ' '.join(self.config['input_path_list'])
        output_file = self.config['output_path']
        command1 = f'zcat {input_files} \\'
        command2 = f'\t| parallel --pipe -j {threads} -k --L {lines} en_erg_preprocess \\'
        command3 = '\t| progress \\'
        command4 = f'\t| pigz -c > {output_file}'
        self += [command1, command2, command3, command4]


class PrepareSubScript(SubScript):
    def make(self):
        group = self.config.get('group', None)
        command = 'run.sh'
        h_rt = self.config['h_rt']
        self.add(command, group, h_rt)


def main():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', dest = 'config', default = 'config.yaml')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    run_script = PrepareRunScript(config)
    with open('run.sh', 'w') as f:
        print(str(run_script), file = f)

    sub_script = PrepareSubScript(config)
    with open('sub.sh', 'w') as f:
        print(str(sub_script), file = f)

