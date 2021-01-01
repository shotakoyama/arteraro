from fa_script.rescore.gleu import GleuRescoreRunScript
from fa_script.rescore.generator import RescoreRegenerateRunScriptGenerator, RescoreScoreRunScriptGenerator
from fa_script.rescore.run import RescoreRegenerateRunScript
from fa_script.rescore.sub import RescoreRegenerateSubScript, RescoreScoreSubScript
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class JflegRescoreRegenerateRunScriptGenerator(RescoreRegenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', RescoreRegenerateRunScript)

class JflegRescoreRegenerateSubScript(RescoreRegenerateSubScript):
    def __init__(self):
        super().__init__('jfleg')

regenerate_run = JflegRescoreRegenerateRunScriptGenerator()
regenerate_sub = OutputSubScriptGenerator(JflegRescoreRegenerateSubScript)

class JflegValidRescoreScoreRunScript(GleuRescoreRunScript):
    def input_path(self):
        reference = ' '.join(self.eval_config['jfleg']['valid_ref'])
        source = self.eval_config['jfleg']['valid_orig']
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        return reference, source, corrected

class JflegTestRescoreScoreRunScript(GleuRescoreRunScript):
    def input_path(self):
        reference = ' '.join(self.eval_config['jfleg']['test_ref'])
        source = self.eval_config['jfleg']['test_orig']
        lmil = int(self.l * 1000)
        corrected = 'best.{}.txt'.format(lmil)
        return reference, source, corrected

class JflegValidRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', 'valid', JflegValidRescoreScoreRunScript)

class JflegTestRescoreScoreRunScriptGenerator(RescoreScoreRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', 'test', JflegTestRescoreScoreRunScript)

class JflegValidRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('jfleg', 'valid')

class JflegTestRescoreScoreSubScript(RescoreScoreSubScript):
    def __init__(self):
        super().__init__('jfleg', 'test')

valid_score_run = JflegValidRescoreScoreRunScriptGenerator()
test_score_run = JflegTestRescoreScoreRunScriptGenerator()
valid_score_sub = OutputSubScriptGenerator(JflegValidRescoreScoreSubScript)
test_score_sub = OutputSubScriptGenerator(JflegTestRescoreScoreSubScript)

jfleg_rescore_regenerate = ScriptGenerator(regenerate_run, regenerate_sub)
jfleg_rescore_valid_score = ScriptGenerator(valid_score_run, valid_score_sub)
jfleg_rescore_test_score = ScriptGenerator(test_score_run, test_score_sub)

