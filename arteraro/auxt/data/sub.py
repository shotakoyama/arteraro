from pathlib import Path
from arteraro.auxt.script import SubScript

class DataSubScript(SubScript):
    def make_workdir(self, script):
        workdir = str(Path(str(script.index)).resolve())
        return workdir

