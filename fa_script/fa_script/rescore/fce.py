from fa_script.rescore.errant import ErrantRescoreRunScript
from fa_script.rescore.generator import RescoreRegenerateRunScriptGenerator, RescoreScoreRunScriptGenerator
from fa_script.rescore.run import RescoreRegenerateRunScript
from fa_script.rescore.sub import RescoreRegenerateSubScript, RescoreScoreSubScript
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class FceRescoreRegenerateRunScriptGenerator(RescoreRegenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', RescoreRegenerateRunScript)

class FceRescoreRegenerateSubScript(RescoreRegenerateSubScript):
    def __init__(self):
        super().__init__('fce')

regenerate_run = FceRescoreRegenerateRunScriptGenerator()
regenerate_sub = OutputSubScriptGenerator(FceRescoreRegenerateSubScript)

class FceValidRescoreScoreRunScript(ErrantRescoreRunScript):
    def input_path(self):
        original = self.eval_config['fce']['valid_orig']
        reference = self.eval_config['fce']['valid_m2']
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        return original, reference, corrected

class FceTestRescoreScoreRunScript(ErrantRescoreRunScript):
    def input_path(self):
        original = self.eval_config['fce']['test_orig']
        reference = self.eval_config['fce']['test_m2']
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        return original, reference, corrected

class FceValidRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', 'valid', FceValidRescoreScoreRunScript)

class FceTestRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', 'test', FceTestRescoreScoreRunScript)

class FceValidRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('fce', 'valid')

class FceTestRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('fce', 'test')

valid_score_run = FceValidRescoreScoreRunScriptGenerator()
test_score_run = FceTestRescoreScoreRunScriptGenerator()
valid_score_sub = OutputSubScriptGenerator(FceValidRescoreScoreSubScript)
test_score_sub = OutputSubScriptGenerator(FceTestRescoreScoreSubScript)

fce_rescore_regenerate = ScriptGenerator(regenerate_run, regenerate_sub)
fce_rescore_valid_score = ScriptGenerator(valid_score_run, valid_score_sub)
fce_rescore_test_score = ScriptGenerator(test_score_run, test_score_sub)

