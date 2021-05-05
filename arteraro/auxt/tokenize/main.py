from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.command import parallel_command
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.run import generate_run

class TokenizeJobScript(JobScript):
    def __init__(self, index):
        self.index = index
        super().__init__()

    def make_path(self):
        return 'tokenize.{}.sh'.format(self.index)

    def make(self):
        j = self.config['threads']
        L = self.config['lines']
        command = parallel_command(j, L, '"en-tokenize"')
        input_path = str(Path(self.config['input_path'] + '.{}.gz'.format(self.index)).resolve())
        output_path = str(Path('tokenized.{}.gz'.format(self.index)).resolve())
        self.append('zcat {} | {} | progress | pigz -c > {}'.format(input_path, command, output_path))

class TokenizeRunScript(RunScript):
    def make_path(self):
        return 'run.sh'

class TokenizeSubScript(SubScript):
    def make_path(self):
        return 'sub.sh'

    def make_node(self):
        return self.sub_config.get('node', 'rt_C.large')

def tokenize():
    config = load_config()
    num_iter = config['iter']

    script_list = [TokenizeJobScript(index) for index in range(num_iter)]
    generate_run(script_list,
            TokenizeRunScript,
            TokenizeSubScript)

