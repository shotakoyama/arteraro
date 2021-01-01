from fa_script.score.errant import ErrantScoreRunScript
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
from fa_script.result.errant import ErrantResultTable
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class FceValidScoreRunScript(ErrantScoreRunScript):
    def input_path(self):
        original = self.eval_config['fce']['valid_orig']
        reference = self.eval_config['fce']['valid_m2']
        corrected = 'best.txt'
        return original, reference, corrected

class FceTestScoreRunScript(ErrantScoreRunScript):
    def input_path(self):
        original = self.eval_config['fce']['test_orig']
        reference = self.eval_config['fce']['test_m2']
        corrected = 'best.txt'
        return original, reference, corrected

class FceValidSingleScoreRunScriptGenerator(ValidSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', FceValidScoreRunScript)

class FceTestSingleScoreRunScriptGenerator(TestSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', FceTestScoreRunScript)

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

class FceValidEnsembleScoreRunScriptGenerator(ValidEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', FceValidScoreRunScript)

class FceTestEnsembleScoreRunScriptGenerator(TestEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', FceTestScoreRunScript)

valid_single_run = FceValidSingleScoreRunScriptGenerator()
test_single_run = FceTestSingleScoreRunScriptGenerator()
valid_ensemble_run = FceValidEnsembleScoreRunScriptGenerator()
test_ensemble_run = FceTestEnsembleScoreRunScriptGenerator()

class FceValidSingleScoreSubScript(ValidSingleScoreSubScript):
    def __init__(self):
        super().__init__('fce')

class FceTestSingleScoreSubScript(TestSingleScoreSubScript):
    def __init__(self):
        super().__init__('fce')

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

class FceValidEnsembleScoreSubScript(ValidEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('fce')

class FceTestEnsembleScoreSubScript(TestEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('fce')

valid_single_sub = OutputSubScriptGenerator(FceValidSingleScoreSubScript)
test_single_sub = OutputSubScriptGenerator(FceTestSingleScoreSubScript)
valid_ensemble_sub = OutputSubScriptGenerator(FceValidEnsembleScoreSubScript)
test_ensemble_sub = OutputSubScriptGenerator(FceTestEnsembleScoreSubScript)

score_fce_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
score_fce_test_single = ScriptGenerator(test_single_run, test_single_sub)
score_fce_valid_ensemble = ScriptGenerator(valid_ensemble_run, valid_ensemble_sub)
score_fce_test_ensemble = ScriptGenerator(test_ensemble_run, test_ensemble_sub)

