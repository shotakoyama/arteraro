from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.result.m2 import M2ResultTableFactory
from .util import (
        valid_single_score,
        test_single_score,
        valid_ensemble_score,
        test_ensemble_score,
        ensemble_reranked_score)

class M2ScoreJobInterface:
    def make_output_name(self):
        return 'result.txt'

    def make(self):
        scorer_path = self.eval_config['conll']['m2_scorer']
        output_name = self.make_output_name()
        self.append('{} {} {} > {}'.format(
            scorer_path,
            self.corrected_path(),
            self.reference_path(),
            self.outdir.make_path(output_name)))

class M2RerankingScoreJobInterface(M2ScoreJobInterface):
    def make_output_name(self):
        return 'result.{}.txt'.format(self.lmil)


### CoNLL 13 (valid) JOB
class CoNLL13ScorePathInterface:
    def reference_path(self):
        return self.eval_config['conll']['valid_m2']

class CoNLL13ScoreJobScript(
        M2ScoreJobInterface,
        CoNLL13ScorePathInterface,
        GECScoreJobScript):
    pass

class CoNLL13RerankingScoreJobScript(
        M2RerankingScoreJobInterface,
        CoNLL13ScorePathInterface,
        GECRerankingScoreJobScript):
    pass


# CoNLL 14 (test) JOB
class CoNLL14ScorePathInterface:
    def reference_path(self):
        return self.eval_config['conll']['test_m2']

class CoNLL14ScoreJobScript(
        M2ScoreJobInterface,
        CoNLL14ScorePathInterface,
        GECScoreJobScript):
    pass

class CoNLL14RerankingScoreJobScript(
        M2RerankingScoreJobInterface,
        CoNLL14ScorePathInterface,
        GECRerankingScoreJobScript):
    pass


# CoNLL 13 (valid) RUN/SUB
class CoNLL13SingleScorePathInterface:
    def make_path(self):
        return 'score_conll_valid.sh'

class CoNLL13SingleScoreRunScript(
        CoNLL13SingleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL13SingleScoreSubScript(
        CoNLL13SingleScorePathInterface,
        ScoreSubScript):
    pass

class CoNLL13EnsembleScorePathInterface:
    def make_path(self):
        return 'score_conll_valid_ensemble.sh'

class CoNLL13EnsembleScoreRunScript(
        CoNLL13EnsembleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL13EnsembleScoreSubScript(
        CoNLL13EnsembleScorePathInterface,
        ScoreSubScript):
    pass

class CoNLL13EnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_conll_valid_ensemble.sh'

class CoNLL13EnsembleRerankedScoreRunScript(
        CoNLL13EnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL13EnsembleRerankedScoreSubScript(
        CoNLL13EnsembleRerankedScorePathInterface,
        ScoreSubScript):
    pass


### CoNLL 14 (test) RUN/SUB
class CoNLL14SingleScorePathInterface:
    def make_path(self):
        return 'score_conll_test.sh'

class CoNLL14SingleScoreRunScript(
        CoNLL14SingleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL14SingleScoreSubScript(
        CoNLL14SingleScorePathInterface,
        ScoreSubScript):
    pass

class CoNLL14EnsembleScorePathInterface:
    def make_path(self):
        return 'score_conll_test_ensemble.sh'

class CoNLL14EnsembleScoreRunScript(
        CoNLL14EnsembleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL14EnsembleScoreSubScript(
        CoNLL14EnsembleScorePathInterface,
        ScoreSubScript):
    pass

class CoNLL14EnsembleRerankedScorePathInterface:
    def make_path(self):
        return 'score_reranked_conll_test_ensemble.sh'

class CoNLL14EnsembleRerankedScoreRunScript(
        CoNLL14EnsembleRerankedScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL14EnsembleRerankedScoreSubScript(
        CoNLL14EnsembleRerankedScorePathInterface,
        ScoreSubScript):
    pass


### score commands
def conll13_single_score():
    valid_single_score('conll',
            CoNLL13ScoreJobScript,
            CoNLL13SingleScoreRunScript,
            CoNLL13SingleScoreSubScript)

def conll14_single_score():
    test_single_score('conll',
            M2ResultTableFactory,
            CoNLL14ScoreJobScript,
            CoNLL14SingleScoreRunScript,
            CoNLL14SingleScoreSubScript)

def conll13_ensemble_score():
    valid_ensemble_score('conll',
            M2ResultTableFactory,
            CoNLL13ScoreJobScript,
            CoNLL13EnsembleScoreRunScript,
            CoNLL13EnsembleScoreSubScript)

def conll14_ensemble_score():
    test_ensemble_score('conll',
            M2ResultTableFactory,
            CoNLL14ScoreJobScript,
            CoNLL14EnsembleScoreRunScript,
            CoNLL14EnsembleScoreSubScript)

def conll13_ensemble_reranked_score():
    ensemble_reranked_score('conll', 'valid',
            CoNLL13RerankingScoreJobScript,
            CoNLL13EnsembleRerankedScoreRunScript,
            CoNLL13EnsembleRerankedScoreSubScript)

def conll14_ensemble_reranked_score():
    ensemble_reranked_score('conll', 'test',
            CoNLL14RerankingScoreJobScript,
            CoNLL14EnsembleRerankedScoreRunScript,
            CoNLL14EnsembleRerankedScoreSubScript)

