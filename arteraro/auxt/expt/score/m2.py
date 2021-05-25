from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.m2 import M2ResultTable

class M2ScoreJobInterface:
    def make(self):
        scorer_path = self.eval_config['conll']['m2_scorer']
        self.append('{} {} {} > {}'.format(
            scorer_path,
            self.corrected_path(),
            self.reference_path(),
            self.outdir.make_path('result.txt')))

class CoNLL13ScoreJobInterface(M2ScoreJobInterface):
    def reference_path(self):
        return self.eval_config['conll']['valid_m2']

class CoNLL14ScoreJobInterface(M2ScoreJobInterface):
    def reference_path(self):
        return self.eval_config['conll']['test_m2']

class CoNLL13ScoreJobScript(
        CoNLL13ScoreJobInterface,
        GECScoreJobScript):
    pass

class CoNLL13RerankingScoreJobScript(
        CoNLL13ScoreJobInterface,
        GECRerankingScoreJobScript):
    pass

class CoNLL14ScoreJobScript(
        CoNLL14ScoreJobInterface,
        GECScoreJobScript):
    pass

class CoNLL14RerankingScoreJobScript(
        CoNLL14ScoreJobInterface,
        GECRerankingScoreJobScript):
    pass

class CoNLL13SingleScorePathInterface:
    def make_path(self):
        return 'score_conll_valid.sh'

class CoNLL14SingleScorePathInterface:
    def make_path(self):
        return 'score_conll_test.sh'

class CoNLL13SingleScoreRunScript(
        CoNLL13SingleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL14SingleScoreRunScript(
        CoNLL14SingleScorePathInterface,
        ScoreRunScript):
    pass

class CoNLL13SingleScoreSubScript(
        CoNLL13SingleScorePathInterface,
        ScoreSubScript):
    pass

class CoNLL14SingleScoreSubScript(
        CoNLL14SingleScorePathInterface,
        ScoreSubScript):
    pass

def conll13_score():
    script_list = [CoNLL13ScoreJobScript(outdir)
            for outdir in get_single_valid_outdir_list('conll')]
    generate_run(script_list,
            CoNLL13SingleScoreRunScript,
            CoNLL13SingleScoreSubScript)

def conll14_score():
    valid_result_table = M2ResultTable('conll', 'valid')
    outdir_list = get_single_test_outdir_list('conll', valid_result_table)
    script_list = [CoNLL14ScoreJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            CoNLL14SingleScoreRunScript,
            CoNLL14SingleScoreSubScript)

