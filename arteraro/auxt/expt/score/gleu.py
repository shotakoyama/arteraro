from .run import ScoreRunScript
from .sub import ScoreSubScript
from .gec_job import GECScoreJobScript, GECRerankingScoreJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.gleu import GLEUResultTable

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

class JFLEGValidScoreJobScript(
        JFLEGValidScoreJobInterface,
        GECScoreJobScript):
    pass

class JFLEGValidRerankingScoreJobScript(
        JFLEGValidScoreJobInterface,
        GECRerankingScoreJobScript):
    pass

class JFLEGTestScoreJobScript(
        JFLEGTestScoreJobInterface,
        GECScoreJobScript):
    pass

class JFLEGTestRerankingScoreJobScript(
        JFLEGTestScoreJobInterface,
        GECRerankingScoreJobScript):
    pass

class JFLEGValidSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_valid.sh'

class JFLEGTestSingleScorePathInterface:
    def make_path(self):
        return 'score_jfleg_test.sh'

class JFLEGValidSingleScoreRunScript(
        JFLEGValidSingleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGTestSingleScoreRunScript(
        JFLEGTestSingleScorePathInterface,
        ScoreRunScript):
    pass

class JFLEGValidSingleScoreSubScript(
        JFLEGValidSingleScorePathInterface,
        ScoreSubScript):
    pass

class JFLEGTestSingleScoreSubScript(
        JFLEGTestSingleScorePathInterface,
        ScoreSubScript):
    pass

def jfleg_valid_score():
    outdir_list = get_single_valid_outdir_list('jfleg')
    script_list = [JFLEGValidScoreJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGValidSingleScoreRunScript,
            JFLEGValidSingleScoreSubScript)

def jfleg_test_score():
    valid_result_table = GLEUResultTable('jfleg', 'valid')
    outdir_list = get_single_test_outdir_list('jfleg', valid_result_table)
    script_list = [JFLEGTestScoreJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGTestSingleScoreRunScript,
            JFLEGTestSingleScoreSubScript)

