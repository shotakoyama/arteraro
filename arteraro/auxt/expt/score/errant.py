from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.result.errant import ErrantResultTableFactory
from .util import (
        valid_single_score,
        test_single_score,
        valid_ensemble_score,
        test_ensemble_score)

class ErrantScoreJobInterface:
    def make_environment_source_path(self):
        return self.eval_config['errant_source_path']

    def make(self):
        output_path = self.outdir.make_path('best.m2')
        self.append('errant_parallel -orig {} -cor {} -out {}'.format(
            self.original_path(),
            self.corrected_path(),
            output_path))
        reference = self.reference_path()
        self.append('errant_compare -ref {} -hyp {} > {}'.format(
            reference, output_path, self.outdir.make_path('result.txt')))
        self.append('errant_compare -ref {} -hyp {} -cat 1 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat1')))
        self.append('errant_compare -ref {} -hyp {} -cat 2 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat2')))
        self.append('errant_compare -ref {} -hyp {} -cat 3 > {}'.format(
            reference, output_path, self.outdir.make_path('result.cat3')))

### BEA19 valid JOB
class BEA19ValidScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['bea19']['valid_orig']

    def reference_path(self):
        return self.eval_config['bea19']['valid_m2']

class BEA19ValidScoreJobScript(
        BEA19ValidScoreJobInterface,
        GECScoreJobScript):
    pass

class BEA19ValidRerankingScoreJobScript(
        BEA19ValidScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


### FCE valid JOB
class FCEValidScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['fce']['valid_orig']

    def reference_path(self):
        return self.eval_config['fce']['valid_m2']

class FCEValidScoreJobScript(
        FCEValidScoreJobInterface,
        GECScoreJobScript):
    pass

class FCEValidRerankingScoreJobScript(
        FCEValidScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


### FCE test JOB
class FCETestScoreJobInterface(ErrantScoreJobInterface):
    def original_path(self):
        return self.eval_config['fce']['test_orig']

    def reference_path(self):
        return self.eval_config['fce']['test_m2']

class FCETestScoreJobScript(
        FCETestScoreJobInterface,
        GECScoreJobScript):
    pass

class FCETestRerankingScoreJobScript(
        FCETestScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


### BEA19 valid RUN/SUB
class BEA19ValidSingleScorePathInterface:
    def make_path(self):
        return 'score_bea19_valid.sh'

class BEA19ValidSingleScoreRunScript(
        BEA19ValidSingleScorePathInterface,
        ScoreRunScript):
    pass

class BEA19ValidSingleScoreSubScript(
        BEA19ValidSingleScorePathInterface,
        ScoreSubScript):
    pass

class BEA19ValidEnsembleScorePathInterface:
    def make_path(self):
        return 'score_bea19_valid_ensemble.sh'

class BEA19ValidEnsembleScoreRunScript(
        BEA19ValidEnsembleScorePathInterface,
        ScoreRunScript):
    pass

class BEA19ValidEnsembleScoreSubScript(
        BEA19ValidEnsembleScorePathInterface,
        ScoreSubScript):
    pass


### FCE valid RUN/SUB
class FCEValidSingleScorePathInterface:
    def make_path(self):
        return 'score_fce_valid.sh'

class FCEValidSingleScoreRunScript(
        FCEValidSingleScorePathInterface,
        ScoreRunScript):
    pass

class FCEValidSingleScoreSubScript(
        FCEValidSingleScorePathInterface,
        ScoreSubScript):
    pass

class FCEValidEnsembleScorePathInterface:
    def make_path(self):
        return 'score_fce_valid_ensemble.sh'

class FCEValidEnsembleScoreRunScript(
        FCEValidEnsembleScorePathInterface,
        ScoreRunScript):
    pass

class FCEValidEnsembleScoreSubScript(
        FCEValidEnsembleScorePathInterface,
        ScoreSubScript):
    pass


### FCE test RUN/SUB
class FCETestSingleScorePathInterface:
    def make_path(self):
        return 'score_fce_test.sh'

class FCETestSingleScoreRunScript(
        FCETestSingleScorePathInterface,
        ScoreRunScript):
    pass

class FCETestSingleScoreSubScript(
        FCETestSingleScorePathInterface,
        ScoreSubScript):
    pass

class FCETestEnsembleScorePathInterface:
    def make_path(self):
        return 'score_fce_test_ensemble.sh'

class FCETestEnsembleScoreRunScript(
        FCETestEnsembleScorePathInterface,
        ScoreRunScript):
    pass

class FCETestEnsembleScoreSubScript(
        FCETestEnsembleScorePathInterface,
        ScoreSubScript):
    pass

### score commands
def bea19_valid_single_score():
    valid_single_score('bea19',
            BEA19ValidScoreJobScript,
            BEA19ValidSingleScoreRunScript,
            BEA19ValidSingleScoreSubScript)

def fce_valid_single_score():
    valid_single_score('fce',
            FCEValidScoreJobScript,
            FCEValidSingleScoreRunScript,
            FCEValidSingleScoreSubScript)

def fce_test_single_score():
    test_single_score('fce',
            ErrantResultTableFactory,
            FCETestScoreJobScript,
            FCETestSingleScoreRunScript,
            FCETestSingleScoreSubScript)

def bea19_valid_ensemble_score():
    valid_ensemble_score('bea19',
            ErrantResultTableFactory,
            BEA19ValidScoreJobScript,
            BEA19ValidEnsembleScoreRunScript,
            BEA19ValidEnsembleScoreSubScript)

def fce_valid_ensemble_score():
    valid_ensemble_score('fce',
            ErrantResultTableFactory,
            FCEValidScoreJobScript,
            FCEValidEnsembleScoreRunScript,
            FCEValidEnsembleScoreSubScript)

def fce_test_ensemble_score():
    test_ensemble_score('fce',
            ErrantResultTableFactory,
            FCETestScoreJobScript,
            FCETestEnsembleScoreRunScript,
            FCETestEnsembleScoreSubScript)

