from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.result.errant import ErrantResultTableFactory
from .util import (
        valid_single_score,
        test_single_score,
        valid_ensemble_score,
        test_ensemble_score,
        ensemble_reranked_score)

class ErrantScoreJobInterface:
    def make_environment_source_path(self):
        return self.eval_config['errant_source_path']

    def make_output_name(self):
        output_name = 'best.m2'
        result_name = 'result.txt'
        cat1_name = 'result.cat1'
        cat2_name = 'result.cat2'
        cat3_name = 'result.cat3'
        return output_name, result_name, cat1_name, cat2_name, cat3_name

    def make(self):
        output_name, result_name, cat1_name, cat2_name, cat3_name = self.make_output_name()
        output_path = self.outdir.make_path(output_name)
        result_path = self.outdir.make_path(result_name)
        cat1_path = self.outdir.make_path(cat1_name)
        cat2_path = self.outdir.make_path(cat2_name)
        cat3_path = self.outdir.make_path(cat3_name)
        self.append('errant_parallel -orig {} -cor {} -out {}'.format(
            self.original_path(), self.corrected_path(), output_path))
        reference = self.reference_path()
        self.append('errant_compare -ref {} -hyp {} > {}'.format(
            reference, output_path, result_path))
        self.append('errant_compare -ref {} -hyp {} -cat 1 > {}'.format(
            reference, output_path, cat1_path))
        self.append('errant_compare -ref {} -hyp {} -cat 2 > {}'.format(
            reference, output_path, cat2_path))
        self.append('errant_compare -ref {} -hyp {} -cat 3 > {}'.format(
            reference, output_path, cat3_path))

class ErrantRerankingScoreJobInterface(ErrantScoreJobInterface):
    def make_output_name(self):
        output_name = 'best.{}.m2'.format(self.lmil)
        result_name = 'result.{}.txt'.format(self.lmil)
        cat1_name = 'result.{}.cat1'.format(self.lmil)
        cat2_name = 'result.{}.cat2'.format(self.lmil)
        cat3_name = 'result.{}.cat3'.format(self.lmil)
        return output_name, result_name, cat1_name, cat2_name, cat3_name


### BEA19 valid JOB
class BEA19ValidScorePathInterface:
    def original_path(self):
        return self.eval_config['bea19']['valid_orig']

    def reference_path(self):
        return self.eval_config['bea19']['valid_m2']

class BEA19ValidScoreJobScript(
        ErrantScoreJobInterface,
        BEA19ValidScorePathInterface,
        GECScoreJobScript):
    pass

class BEA19ValidRerankingScoreJobScript(
        ErrantRerankingScoreJobInterface,
        BEA19ValidScorePathInterface,
        GECRerankingScoreJobScript):
    pass


### FCE valid JOB
class FCEValidScorePathInterface:
    def original_path(self):
        return self.eval_config['fce']['valid_orig']

    def reference_path(self):
        return self.eval_config['fce']['valid_m2']

class FCEValidScoreJobScript(
        ErrantScoreJobInterface,
        FCEValidScorePathInterface,
        GECScoreJobScript):
    pass

class FCEValidRerankingScoreJobScript(
        ErrantRerankingScoreJobInterface,
        FCEValidScorePathInterface,
        GECRerankingScoreJobScript):
    pass


### FCE test JOB
class FCETestScorePathInterface:
    def original_path(self):
        return self.eval_config['fce']['test_orig']

    def reference_path(self):
        return self.eval_config['fce']['test_m2']

class FCETestScoreJobScript(
        ErrantScoreJobInterface,
        FCETestScorePathInterface,
        GECScoreJobScript):
    pass

class FCETestRerankingScoreJobScript(
        ErrantRerankingScoreJobInterface,
        FCETestScorePathInterface,
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

class BEA19ValidEnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_bea19_valid_ensemble.sh'

class BEA19ValidEnsembleRerankedScoreRunScript(
        BEA19ValidEnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class BEA19ValidEnsembleRerankedScoreSubScript(
        BEA19ValidEnsembleRerankedScorePathInterface,
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

class FCEValidEnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_fce_valid_ensemble.sh'

class FCEValidEnsembleRerankedScoreRunScript(
        FCEValidEnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class FCEValidEnsembleRerankedScoreSubScript(
        FCEValidEnsembleRerankedScorePathInterface,
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

class FCETestEnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_fce_test_ensemble.sh'

class FCETestEnsembleRerankedScoreRunScript(
        FCETestEnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class FCETestEnsembleRerankedScoreSubScript(
        FCETestEnsembleRerankedScorePathInterface,
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

def bea19_valid_ensemble_reranked_score():
    ensemble_reranked_score('bea19', 'valid',
            BEA19ValidRerankingScoreJobScript,
            BEA19ValidEnsembleRerankedScoreRunScript,
            BEA19ValidEnsembleRerankedScoreSubScript)

def fce_valid_ensemble_reranked_score():
    ensemble_reranked_score('fce', 'valid',
            FCEValidRerankingScoreJobScript,
            FCEValidEnsembleRerankedScoreRunScript,
            FCEValidEnsembleRerankedScoreSubScript)

def fce_test_ensemble_reranked_score():
    ensemble_reranked_score('fce', 'test',
            FCETestRerankingScoreJobScript,
            FCETestEnsembleRerankedScoreRunScript,
            FCETestEnsembleRerankedScoreSubScript)

