from pathlib import Path
from arteraro.auxt.script import SubScript

class TrainSubScript(SubScript):
    def make_workdir(self, script):
        workdir = str(Path(str(script.index)).resolve())
        return workdir

    def make_path(self):
        return 'train.sh'

    def make_h_rt(self):
        return self.sub_config['train']['h_rt']

    def make_node(self):
        return self.sub_config['train']['node']

    def make_num_node(self):
        return self.sub_config['train']['num_node']

