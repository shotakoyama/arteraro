from pathlib import Path
from arteraro.auxt.script import JobScript, RunScript, SubScript
from arteraro.auxt.util.load import load_config
from arteraro.auxt.util.run import generate_run

class RTTMergeJobScript(JobScript):
    localdir = True

    def __init__(self, index):
        self.index = index
        super().__init__()

    def make_path(self):
        return '{}/merge.sh'.format(self.index)

    def make(self):
        pass

def rtt_merge():
    print('rtt_merge')

