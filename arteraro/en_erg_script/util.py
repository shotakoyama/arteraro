from pathlib import Path

def spm_command(spm_model, dropout = None):
    line = 'pyspm_encode --model_file {}'.format(Path(spm_model).resolve())
    if dropout is not None:
        line += f' --dropout {dropout}'
    return line

def qsub_command(code_path, group, h_rt, node, num_node, var_dict=None):
    line = 'qsub'
    if group is not None:
        line += f' -g {group}'
    line += f' -l {node}={num_node}'
    line += f' -l h_rt={h_rt}'
    if var_dict is not None:
        line += ' -v ' + ','.join([f'{key}={value}' for key, value in var_dict.items()])
    line += f' {code_path}'
    return line

class Script(list):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.header()
        self.make()

    def make(self):
        raise NotImplementedError

    def __str__(self):
        return '\n'.join(self)


class RunScript(Script):
    def header_workdir(self):
        self.append('if [[ -z $WORKDIR ]] ; then')
        self.append('   WORKDIR=`dirname $0`')
        self.append('fi')
        self.append('cd $WORKDIR')

    def header_environment(self):
        self.append('if [[ -n $IS_SGE ]] ; then')
        self.append('   . /etc/profile.d/modules.sh')
        if 'source_path' in self.config:
            self.append('   . {}'.format(Path(self.config['source_path']).resolve()))
        self.append('fi')

    def header_localdir(self):
        self.append('if [[ -z $SGE_LOCALDIR ]] ; then')
        self.append('   mkdir tmp')
        self.append('   SGE_LOCALDIR=tmp')
        self.append('fi')

    def header(self):
        self.append('set -ex')
        self.append('') # blank line
        self.header_workdir()
        self.append('')
        self.header_environment()
        self.append('')
        self.header_localdir()
        self.append('')


class SubScript(Script):
    def header(self):
        self.append('set -ex')
        self.append('')
        self.append('BASEDIR=$(cd $(dirname $0) ; pwd)')
        self.append('')

