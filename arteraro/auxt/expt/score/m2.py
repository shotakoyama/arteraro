from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.result.m2 import M2ResultTableFactory
from .util import (
        valid_single_score,
        test_single_score,
        valid_ensemble_score,
        test_ensemble_score)

class M2ScoreJobInterface:
    def make(self):
        scorer_path = self.eval_config['conll']['m2_scorer']
        self.append('{} {} {} > {}'.format(
            scorer_path,
            self.corrected_path(),
            self.reference_path(),
            self.outdir.make_path('result.txt')))

### CoNLL 13 (valid) JOB
class CoNLL13ScoreJobInterface(M2ScoreJobInterface):
    def reference_path(self):
        return self.eval_config['conll']['valid_m2']

class CoNLL13ScoreJobScript(
        CoNLL13ScoreJobInterface,
        GECScoreJobScript):
    pass

class CoNLL13RerankingScoreJobScript(
        CoNLL13ScoreJobInterface,
        GECRerankingScoreJobScript):
    pass


# CoNLL 14 (test) JOB
class CoNLL14ScoreJobInterface(M2ScoreJobInterface):
    def reference_path(self):
        return self.eval_config['conll']['test_m2']

class CoNLL14ScoreJobScript(
        CoNLL14ScoreJobInterface,
        GECScoreJobScript):
    pass

class CoNLL14RerankingScoreJobScript(
        CoNLL14ScoreJobInterface,
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

