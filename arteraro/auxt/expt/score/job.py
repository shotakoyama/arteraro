from pathlib import Path
from arteraro.auxt.expt.job import ExptJobScript

class ScoreJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('score.sh')

