from fa_script.score.m2 import M2ScoreRunScript
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
from fa_script.result.m2 import M2ResultTable
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class Conll13ScoreRunScript(M2ScoreRunScript):
    def input_path(self):
        corrected = 'best.txt'
        reference = self.eval_config['conll']['valid_m2']
        return corrected, reference

class Conll14ScoreRunScript(M2ScoreRunScript):
    def input_path(self):
        corrected = 'best.txt'
        reference = self.eval_config['conll']['test_m2']
        return corrected, reference

class Conll13SingleScoreRunScriptGenerator(ValidSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', Conll13ScoreRunScript)

class Conll14SingleScoreRunScriptGenerator(TestSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', Conll14ScoreRunScript)

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

class Conll13EnsembleScoreRunScriptGenerator(ValidEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', Conll13ScoreRunScript)

class Conll14EnsembleScoreRunScriptGenerator(TestEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', Conll14ScoreRunScript)

valid_single_run = Conll13SingleScoreRunScriptGenerator()
test_single_run = Conll14SingleScoreRunScriptGenerator()
valid_ensemble_run = Conll13EnsembleScoreRunScriptGenerator()
test_ensemble_run = Conll14EnsembleScoreRunScriptGenerator()

class Conll13SingleScoreSubScript(ValidSingleScoreSubScript):
    def __init__(self):
        super().__init__('conll')

class Conll14SingleScoreSubScript(TestSingleScoreSubScript):
    def __init__(self):
        super().__init__('conll')

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

class Conll13EnsembleScoreSubScript(ValidEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('conll')

class Conll14EnsembleScoreSubScript(TestEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('conll')

valid_single_sub = OutputSubScriptGenerator(Conll13SingleScoreSubScript)
test_single_sub = OutputSubScriptGenerator(Conll14SingleScoreSubScript)
valid_ensemble_sub = OutputSubScriptGenerator(Conll13EnsembleScoreSubScript)
test_ensemble_sub = OutputSubScriptGenerator(Conll14EnsembleScoreSubScript)

score_conll_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
score_conll_test_single = ScriptGenerator(test_single_run, test_single_sub)
score_conll_valid_ensemble = ScriptGenerator(valid_ensemble_run, valid_ensemble_sub)
score_conll_test_ensemble = ScriptGenerator(test_ensemble_run, test_ensemble_sub)

