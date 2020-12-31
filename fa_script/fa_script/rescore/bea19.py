from fa_script.rescore.errant import ErrantRescoreRunScript
from fa_script.rescore.generator import RescoreRegenerateRunScriptGenerator, RescoreScoreRunScriptGenerator
from fa_script.rescore.run import RescoreRegenerateRunScript
from fa_script.rescore.sub import RescoreRegenerateSubScript, RescoreScoreSubScript
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class Bea19RescoreRegenerateRunScriptGenerator(RescoreRegenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', RescoreRegenerateRunScript)

class Bea19RescoreRegenerateSubScript(RescoreRegenerateSubScript):
    def __init__(self):
        super().__init__('bea19')

regenerate_run = Bea19RescoreRegenerateRunScriptGenerator()
regenerate_sub = OutputSubScriptGenerator(Bea19RescoreRegenerateSubScript)

class Bea19ValidRescoreScoreRunScript(ErrantRescoreRunScript):
    def input_path(self):
        original = self.eval_config['bea19']['valid_orig']
        reference = self.eval_config['bea19']['valid_m2']
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        return original, reference, corrected

class Bea19ValidRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', 'valid', Bea19ValidRescoreScoreRunScript)

class Bea19ValidRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('bea19', 'valid')

valid_score_run = Bea19ValidRescoreScoreRunScriptGenerator()
valid_score_sub = OutputSubScriptGenerator(Bea19ValidRescoreScoreSubScript)

bea19_rescore_regenerate = ScriptGenerator(regenerate_run, regenerate_sub)
bea19_rescore_valid_score = ScriptGenerator(valid_score_run, valid_score_sub)

