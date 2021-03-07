from pathlib import Path
from arteraro.fa_script.util.name import make_script_name
from arteraro.fa_script.util.load import load_config, load_sub_config

class Script(list):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.header()
        self.make()

    def __str__(self):
        return '\n'.join(self)

class RunScript(Script):
    def __init__(self, work_dir, use_localdir=False):
        self.work_dir = work_dir
        self.use_localdir = use_localdir
        super().__init__()

    def header_workdir(self):
        self.append('cd {}'.format(self.work_dir))

    def append_source_path(self):
        if 'source_path' in self.config:
            path = Path(self.config['source_path']).resolve()
            self.append('   . {}'.format(path))

    def header_environment(self):
        self += [
            'if [[ -n $IS_SGE ]] ; then',
            '   . /etc/profile.d/modules.sh']
        self.append_source_path()
        self.append('fi')

    def header_localdir(self):
        self += [
            'if [[ -z $SGE_LOCALDIR ]] ; then',
            '   mkdir tmp',
            '   SGE_LOCALDIR=tmp',
            'fi']

    def header(self):
        self.append('set -ex')
        self.append('') # blank line
        self.header_workdir()
        self.append('')
        self.header_environment()
        self.append('')
        if self.use_localdir:
            self.header_localdir()
            self.append('')

class SubScript(Script):
    def __init__(self):
        self.sub_config = load_sub_config()
        super().__init__()

    def header(self):
        self.append('set -ex')
        self.append('')

