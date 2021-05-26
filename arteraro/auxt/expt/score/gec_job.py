import yaml
from pathlib import Path
from .job import ScoreJobScript
from arteraro.auxt.expt.job import ExptGECJobScriptInterface

class GECScoreJobScript(ExptGECJobScriptInterface, ScoreJobScript):
    def corrected_path(self):
        return self.outdir.make_path('best.txt')

class GECRerankingScoreJobScript(GECScoreJobScript):
    def __init__(self, outdir, l):
        self.l = l
        self.lmil = int(self.l * 1000)
        super().__init__(outdir)

    def corrected_path(self):
        return self.outdir.make_path('best.{}.txt'.format(self.lmil))

    def make_path(self):
        return self.outdir.make_path('score.{}.sh'.format(self.lmil))

