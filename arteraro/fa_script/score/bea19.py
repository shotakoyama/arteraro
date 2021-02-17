from arteraro.fa_script.score.errant import ErrantScoreRunScript
from arteraro.fa_script.score.generator import ValidSingleScoreRunScriptGenerator, ValidEnsembleScoreRunScriptGenerator
from arteraro.fa_script.score.sub import ValidSingleScoreSubScript, ValidEnsembleScoreSubScript
from arteraro.fa_script.util.output import OutputSubScriptGenerator
from arteraro.fa_script.util.generator import ScriptGenerator

class Bea19ScoreRunScript(ErrantScoreRunScript):
    def input_path(self):
        original = self.eval_config['bea19']['valid_orig']
        reference = self.eval_config['bea19']['valid_m2']
        corrected = 'best.txt'
        return original, reference, corrected

class Bea19ValidSingleScoreRunScriptGenerator(ValidSingleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', Bea19ScoreRunScript)

class Bea19ValidEnsembleScoreRunScriptGenerator(ValidEnsembleScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', Bea19ScoreRunScript)

valid_single_run = Bea19ValidSingleScoreRunScriptGenerator()
valid_ensemble_run = Bea19ValidEnsembleScoreRunScriptGenerator()

class Bea19ValidSingleScoreSubScript(ValidSingleScoreSubScript):
    def __init__(self):
        super().__init__('bea19')

class Bea19ValidEnsembleScoreSubScript(ValidEnsembleScoreSubScript):
    def __init__(self):
        super().__init__('bea19')

valid_single_sub = OutputSubScriptGenerator(Bea19ValidSingleScoreSubScript)
valid_ensemble_sub = OutputSubScriptGenerator(Bea19ValidEnsembleScoreSubScript)

score_bea19_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
score_bea19_valid_ensemble = ScriptGenerator(valid_ensemble_run, valid_ensemble_sub)

