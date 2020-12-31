from fa_script.generate.generator import(
        ValidSingleGenerateRunScriptGenerator,
        TestSingleGenerateRunScriptGenerator,
        EnsembleGenerateRunScriptGenerator)
from fa_script.generate.run import GenerateRunScript
from fa_script.generate.sub import (
        ValidSingleGenerateSubScript,
        TestSingleGenerateSubScript,
        EnsembleGenerateSubScript)
from fa_script.result.errant import M2ResultTable
from fa_script.util.output import OutputSubScriptGenerator
from fa_script.util.generator import ScriptGenerator

class Bea19ValidSingleGenerateRunScriptGenerator(ValidSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', GenerateRunScript)
        self.buffer_size = 4384
        self.source = self.eval_config['bea19']['valid_src']

class Bea19TestSingleGenerateRunScriptGenerator(TestSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', GenerateRunScript)
        self.buffer_size = 4477
        self.source = self.eval_config['bea19']['test_src']

    def make_result_table(self):
        return M2ResultTable(self.config, self.dataset, 'valid')

class Bea19EnsembleGenerateRunScriptGenerator(EnsembleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('bea19', GenerateRunScript)
        self.valid_buffer_size = 4384
        self.test_buffer_size = 4477
        self.valid_source = self.eval_config['bea19']['valid_src']
        self.test_source = self.eval_config['bea19']['test_src']

    def make_result_table(self):
        return M2ResultTable(self.config, self.dataset, 'valid')

valid_single_run = Bea19ValidSingleGenerateRunScriptGenerator()
test_single_run = Bea19TestSingleGenerateRunScriptGenerator()
ensemble_run = Bea19EnsembleGenerateRunScriptGenerator()

class Bea19ValidSingleGenerateSubScript(ValidSingleGenerateSubScript):
    def __init__(self):
        super().__init__('bea19')

class Bea19TestSingleGenerateSubScript(TestSingleGenerateSubScript):
    def __init__(self):
        super().__init__('bea19')

    def make_result_table(self):
        return M2ResultTable(self.config, self.dataset, 'valid')

class Bea19EnsembleGenerateSubScript(EnsembleGenerateSubScript):
    def __init__(self):
        super().__init__('bea19')

    def make_result_table(self):
        return M2ResultTable(self.config, self.dataset, 'valid')

valid_single_sub = OutputSubScriptGenerator(Bea19ValidSingleGenerateSubScript)
test_single_sub = OutputSubScriptGenerator(Bea19TestSingleGenerateSubScript)
ensemble_sub = OutputSubScriptGenerator(Bea19EnsembleGenerateSubScript)

bea19_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
bea19_test_single = ScriptGenerator(test_single_run, test_single_sub)
bea19_ensemble = ScriptGenerator(ensemble_run, ensemble_sub)

