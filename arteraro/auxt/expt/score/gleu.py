from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.result.gleu import GLEUResultTableFactory
from .util import (
        valid_single_score,
        test_single_score,
        valid_ensemble_score,
        test_ensemble_score,
        ensemble_reranked_score)

class GLEUScoreJobInterface:
    def make(self):
        scorer_path = self.eval_config['jfleg']['gleu_scorer']
        self.append('python {} -r {} -s {} --hyp {} > {}'.format(
            scorer_path,
            self.reference_path(),
            self.original_path(),
            self.corrected_path(),
            self.outdir.make_path('result.txt')))

### JFLEG valid JOB
class JFLEGValidScoreJobInterface(GLEUScoreJobInterface):
    def original_path(self):
        return self.eval_config['jfleg']['valid_orig']

    def reference_path(self):
        return ' '.join(self.eval_config['jfleg']['valid_ref'])

class JFLEGValidScoreJobScript(
        JFLEGValidScoreJobInterface,
        GECScoreJobScript):
    pass

class JFLEGValidRerankingScoreJobScript(
        JFLEGValidScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


### JFLEG test JOB
class JFLEGTestScoreJobInterface(GLEUScoreJobInterface):
    def original_path(self):
        return self.eval_config['jfleg']['test_orig']

    def reference_path(self):
        return ' '.join(self.eval_config['jfleg']['test_ref'])

class JFLEGTestScoreJobScript(
        JFLEGTestScoreJobInterface,
        GECScoreJobScript):
    pass

class JFLEGTestRerankingScoreJobScript(
        JFLEGTestScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


### JFLEG valid RUN/SUB
class JFLEGValidSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_valid.sh'

class JFLEGValidSingleScoreRunScript(
        JFLEGValidSingleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGValidSingleScoreSubScript(
        JFLEGValidSingleScorePathInterface,
        ScoreSubScript):
    pass

class JFLEGValidEnsembleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_valid_ensemble.sh'

class JFLEGValidEnsembleScoreRunScript(
        JFLEGValidEnsembleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGValidEnsembleScoreSubScript(
        JFLEGValidEnsembleScorePathInterface,
        ScoreSubScript):
    pass

class JFLEGValidEnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_jfleg_valid_ensemble.sh'

class JFLEGValidEnsembleRerankedScoreRunScript(
        JFLEGValidEnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGValidEnsembleRerankedScoreSubScript(
        JFLEGValidEnsembleRerankedScorePathInterface,
        ScoreSubScript):
    pass


### JFLEG test RUN/SUB
class JFLEGTestSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_test.sh'

class JFLEGTestSingleScoreRunScript(
        JFLEGTestSingleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGTestSingleScoreSubScript(
        JFLEGTestSingleScorePathInterface,
        ScoreSubScript):
    pass

class JFLEGTestEnsembleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_test_ensemble.sh'

class JFLEGTestEnsembleScoreRunScript(
        JFLEGTestEnsembleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGTestEnsembleScoreSubScript(
        JFLEGTestEnsembleScorePathInterface,
        ScoreSubScript):
    pass

class JFLEGTestEnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_jfleg_test_ensemble.sh'

class JFLEGTestEnsembleRerankedScoreRunScript(
        JFLEGTestEnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGTestEnsembleRerankedScoreSubScript(
        JFLEGTestEnsembleRerankedScorePathInterface,
        ScoreSubScript):
    pass


### score commands
def jfleg_valid_single_score():
    valid_single_score('jfleg',
            JFLEGValidScoreJobScript,
            JFLEGValidSingleScoreRunScript,
            JFLEGValidSingleScoreSubScript)

def jfleg_test_single_score():
    test_single_score('jfleg',
            GLEUResultTableFactory,
            JFLEGTestScoreJobScript,
            JFLEGTestSingleScoreRunScript,
            JFLEGTestSingleScoreSubScript)

def jfleg_valid_ensemble_score():
    valid_ensemble_score('jfleg',
            GLEUResultTableFactory,
            JFLEGValidScoreJobScript,
            JFLEGValidEnsembleScoreRunScript,
            JFLEGValidEnsembleScoreSubScript)

def jfleg_test_ensemble_score():
    test_ensemble_score('jfleg',
            GLEUResultTableFactory,
            JFLEGTestScoreJobScript,
            JFLEGTestEnsembleScoreRunScript,
            JFLEGTestEnsembleScoreSubScript)

def jfleg_valid_ensemble_reranked_score():
    ensemble_reranked_score('jfleg', 'valid',
            JFLEGValidRerankingScoreJobScript,
            JFLEGValidEnsembleRerankedScoreRunScript,
            JFLEGValidEnsembleRerankedScoreSubScript)

def jfleg_test_ensemble_reranked_score():
    ensemble_reranked_score('jfleg', 'test',
            JFLEGTestRerankingScoreJobScript,
            JFLEGTestEnsembleRerankedScoreRunScript,
            JFLEGTestEnsembleRerankedScoreSubScript)

