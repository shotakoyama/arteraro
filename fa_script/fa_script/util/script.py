from pathlib import Path

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
        self += [
            'if [ -z $WORKDIR ] ; then',
            '   WORKDIR=`dirname $0`',
            'fi',
            'cd $WORKDIR']

    def header_environment(self):
        self += [
            'if [ -n $SGE_QSUB ] ; then',
            '   . /etc/profile.d/modules.sh']
        if 'source_path' in self.config:
            path = Path(self.config['source_path']).resolve()
            self.append('   . {}'.format(path))
        self.append('fi')

    def header_localdir(self):
        self += [
            'if [ -z $SGE_LOCALDIR ] ; then',
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
        self.header_localdir()
        self.append('')

class SubScript(Script):
    def __init__(self, config, sub_config):
        self.sub_config = sub_config
        super().__init__(config)

    def header(self):
        self.append('set -ex')
        self.append('')
        self.append('BASEDIR=$(cd $(dirname $0) ; pwd)')
        self.append('')

