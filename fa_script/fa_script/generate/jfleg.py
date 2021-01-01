from fa_script.generate.generator import (
        ValidSingleGenerateRunScriptGenerator,
        TestSingleGenerateRunScriptGenerator,
        EnsembleGenerateRunScriptGenerator)
from fa_script.generate.run import GenerateRunScript
from fa_script.generate.sub import (
        ValidSingleGenerateSubScript,
        TestSingleGenerateSubScript,
        EnsembleGenerateSubScript)
from fa_script.result.gleu import GleuResultTable
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class JflegValidSingleGenerateRunScriptGenerator(ValidSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', GenerateRunScript)
        self.buffer_size = 754
        self.source = self.eval_config['jfleg']['valid_src']

class JflegTestSingleGenerateRunScriptGenerator(TestSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', GenerateRunScript)
        self.buffer_size = 747
        self.source = self.eval_config['jfleg']['test_src']

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

class JflegEnsembleGenerateRunSCriptGenerator(EnsembleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('jfleg', GenerateRunScript)
        self.valid_buffer_size = 754
        self.test_buffer_size = 747
        self.valid_source = self.eval_config['jfleg']['valid_src']
        self.test_source = self.eval_config['jfleg']['test_src']

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

valid_single_run = JflegValidSingleGenerateRunScriptGenerator()
test_single_run = JflegTestSingleGenerateRunScriptGenerator()
ensemble_run = JflegEnsembleGenerateRunSCriptGenerator()

class JflegValidSingleGenerateSubScript(ValidSingleGenerateSubScript):
    def __init__(self):
        super().__init__('jfleg')

class JflegTestSingleGenerateSubScript(TestSingleGenerateSubScript):
    def __init__(self):
        super().__init__('jfleg')

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

class JflegEnsembleGenerateSubScript(EnsembleGenerateSubScript):
    def __init__(self):
        super().__init__('jfleg')

    def make_result_table(self):
        return GleuResultTable(self.dataset, 'valid')

valid_single_sub = OutputSubScriptGenerator(JflegValidSingleGenerateSubScript)
test_single_sub = OutputSubScriptGenerator(JflegTestSingleGenerateSubScript)
ensemble_sub = OutputSubScriptGenerator(JflegEnsembleGenerateSubScript)

generate_jfleg_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
generate_jfleg_test_single = ScriptGenerator(test_single_run, test_single_sub)
generate_jfleg_ensemble = ScriptGenerator(ensemble_run, ensemble_sub)

