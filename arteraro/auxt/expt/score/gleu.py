from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript

class GLEUScoreJobInterface:
    def make(self):
        scorer_path = self.eval_config['jfleg']['gleu_scorer']
        self.append('python {} -r {} -s {} --hyp {} > {}'.format(
            scorer_path,
            self.reference_path(),
            self.original_path(),
            self.corrected_path(),
            self.outdir.make_path('result.txt')))

class JFLEGValidScoreJobInterface(GLEUScoreJobInterface):
    def original_path(self):
        return self.eval_config['jfleg']['valid_orig']

    def reference_path(self):
        return ' '.join(self.eval_config['jfleg']['valid_ref'])

class JFLEGTestScoreJobInterface(GLEUScoreJobInterface):
    def original_path(self):
        return self.eval_config['jfleg']['test_orig']

    def reference_path(self):
        return ' '.join(self.eval_config['jfleg']['test_ref'])

class JFLEGValidScoreJobScript(JFLEGValidScoreJobInterface, GECScoreJobScript):
    pass

class JFLEGValidRerankingScoreJobScript(JFLEGValidScoreJobInterface, GECRerankingScoreJobScript):
    pass

class JFLEGTestScoreJobScript(JFLEGTestScoreJobInterface, GECScoreJobScript):
    pass

class JFLEGTestRerankingScoreJobScript(JFLEGTestScoreJobInterface, GECRerankingScoreJobScript):
    pass

class JFLEGValidSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_valid.sh'

class JFLEGTestSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_test.sh'

class JFLEGValidSingleScoreRunScript(JFLEGValidSingleScorePathInterface, ScoreRunScript):
    pass

class JFLEGTestSingleScoreRunScript(JFLEGTestSingleScorePathInterface, ScoreRunScript):
    pass

class JFLEGValidSingleScoreSubScript(JFLEGValidSingleScorePathInterface, ScoreSubScript):
    pass

class JFLEGTestSingleScoreSubScript(JFLEGTestSingleScorePathInterface, ScoreSubScript):
    pass

