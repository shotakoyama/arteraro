from fa_script.rescore.m2 import M2RescoreRunScript
from fa_script.rescore.generator import RescoreRegenerateRunScriptGenerator, RescoreScoreRunScriptGenerator
from fa_script.rescore.run import RescoreRegenerateRunScript
from fa_script.rescore.sub import RescoreRegenerateSubScript, RescoreScoreSubScript
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class ConllRescoreRegenerateRunScriptGenerator(RescoreRegenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', RescoreRegenerateRunScript)

class ConllRescoreRegenerateSubScript(RescoreRegenerateSubScript):
    def __init__(self):
        super().__init__('conll')

regenerate_run = ConllRescoreRegenerateRunScriptGenerator()
regenerate_sub = OutputSubScriptGenerator(ConllRescoreRegenerateSubScript)

class ConllValidRescoreScoreRunScript(M2RescoreRunScript):
    def input_path(self):
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        reference = self.eval_config['conll']['valid_m2']
        return corrected, reference

class ConllTestRescoreScoreRunScript(M2RescoreRunScript):
    def input_path(self):
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        reference = self.eval_config['conll']['test_m2']
        return corrected, reference

class ConllValidRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', 'valid', ConllValidRescoreScoreRunScript)

class ConllTestRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', 'test', ConllTestRescoreScoreRunScript)

class ConllValidRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('conll', 'valid')

class ConllTestRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('conll', 'test')

valid_score_run = ConllValidRescoreScoreRunScriptGenerator()
test_score_run = ConllTestRescoreScoreRunScriptGenerator()
valid_score_sub = OutputSubScriptGenerator(ConllValidRescoreScoreSubScript)
test_score_sub = OutputSubScriptGenerator(ConllTestRescoreScoreSubScript)

conll_rescore_regenerate = ScriptGenerator(regenerate_run, regenerate_sub)
conll_rescore_valid_score = ScriptGenerator(valid_score_run, valid_score_sub)
conll_rescore_test_score = ScriptGenerator(test_score_run, test_score_sub)

