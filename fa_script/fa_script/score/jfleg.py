from fa_script.score.gleu import GleuScoreRunScript
from fa_script.score.generator import (
        ValidSingleScoreRunScriptGenerator,
        TestSingleScoreRunScriptGenerator,
        ValidEnsembleScoreRunScriptGenerator,
        TestEnsembleScoreRunScriptGenerator)
from fa_script.score.sub import (
        ValidSingleScoreSubScript,
        TestSingleScoreSubScript,
        ValidEnsembleScoreSubScript,
        TestEnsembleScoreSubScript)
from fa_script.result.gleu import GleuResultTable
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class JflegValidScoreRunScript(GleuScoreRunScript):
    def input_path(self):
        reference = ' '.join(self.eval_config['jfleg']['valid_ref'])
        source = self.eval_config['jfleg']['valid_orig']
        corrected = 'best.txt'
        return reference, source, corrected

class JflegTestScoreRunScript(GleuScoreRunScript):
    def input_path(self):
        reference = ' '.join(self.eval_config['jfleg']['test_ref'])
        source = self.eval_config['jfleg']['test_orig']
        corrected = 'best.txt'
        return reference, source, corrected

class JflegValidSingleScoreRunScriptGenerator(ValidSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', JflegValidScoreRunScript)

class JflegTestSingleScoreRunScriptGenerator(TestSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', JflegTestScoreRunScript)

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

class JflegValidEnsembleScoreRunScriptGenerator(ValidEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', JflegValidScoreRunScript)

class JflegTestEnsembleScoreRunScriptGenerator(TestEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', JflegTestScoreRunScript)

valid_single_run = JflegValidSingleScoreRunScriptGenerator()
test_single_run = JflegTestSingleScoreRunScriptGenerator()
valid_ensemble_run = JflegValidEnsembleScoreRunScriptGenerator()
test_ensemble_run = JflegTestEnsembleScoreRunScriptGenerator()

class JflegValidSingleScoreSubScript(ValidSingleScoreSubScript):
    def __init__(self):
        super().__init__('jfleg')

class JflegTestSingleScoreSubScript(TestSingleScoreSubScript):
    def __init__(self):
        super().__init__('jfleg')

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

class JflegValidEnsembleScoreSubScript(ValidEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('jfleg')

class JflegTestEnsembleScoreSubScript(TestEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('jfleg')

valid_single_sub = OutputSubScriptGenerator(JflegValidSingleScoreSubScript)
test_single_sub = OutputSubScriptGenerator(JflegTestSingleScoreSubScript)
valid_ensemble_sub = OutputSubScriptGenerator(JflegValidEnsembleScoreSubScript)
test_ensemble_sub = OutputSubScriptGenerator(JflegTestEnsembleScoreSubScript)

score_jfleg_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
score_jfleg_test_single = ScriptGenerator(test_single_run, test_single_sub)
score_jfleg_valid_ensemble = ScriptGenerator(valid_ensemble_run, valid_ensemble_sub)
score_jfleg_test_ensemble = ScriptGenerator(test_ensemble_run, test_ensemble_sub)

