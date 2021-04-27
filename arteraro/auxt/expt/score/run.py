from arteraro.auxt.script import RunScript

class ScoreRunScript(RunScript):
    pass

class ValidScoreRunScript(ScoreRunScript):
    def make_path(self):
        return 'score_valid.sh'

class TestScoreRunScript(ScoreRunScript):
    def make_path(self):
        return 'score_test.sh'

class EnsembleScoreRunScript(ScoreRunScript):
    def make_path(self):
        return 'score_ensemble.sh'

