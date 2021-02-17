from arteraro.fa_script.generate.generator import(
        ValidSingleGenerateRunScriptGenerator,
        TestSingleGenerateRunScriptGenerator,
        EnsembleGenerateRunScriptGenerator)
from arteraro.fa_script.generate.run import GenerateRunScript
from arteraro.fa_script.generate.sub import (
        ValidSingleGenerateSubScript,
        TestSingleGenerateSubScript,
        EnsembleGenerateSubScript)
from arteraro.fa_script.result.errant import ErrantResultTable
from arteraro.fa_script.util.output import OutputSubScriptGenerator
from arteraro.fa_script.util.generator import ScriptGenerator

class FceValidSingleGenerateRunScriptGenerator(ValidSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', GenerateRunScript)
        self.buffer_size = 2191
        self.source = self.eval_config['fce']['valid_src']

class FceTestSingleGenerateRunScriptGenerator(TestSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', GenerateRunScript)
        self.buffer_size = 2695
        self.source = self.eval_config['fce']['test_src']

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

class FceEnsembleGenerateRunScriptGenerator(EnsembleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('fce', GenerateRunScript)
        self.valid_buffer_size = 2192
        self.test_buffer_size = 2695
        self.valid_source = self.eval_config['fce']['valid_src']
        self.test_source = self.eval_config['fce']['test_src']

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

valid_single_run = FceValidSingleGenerateRunScriptGenerator()
test_single_run = FceTestSingleGenerateRunScriptGenerator()
ensemble_run = FceEnsembleGenerateRunScriptGenerator()

class FceValidSingleGenerateSubScript(ValidSingleGenerateSubScript):
    def __init__(self):
        super().__init__('fce')

class FceTestSingleGenerateSubScript(TestSingleGenerateSubScript):
    def __init__(self):
        super().__init__('fce')

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

class FceEnsembleGenerateSubScript(EnsembleGenerateSubScript):
    def __init__(self):
        super().__init__('fce')

    def make_result_table(self):
        return ErrantResultTable(self.dataset, 'valid')

valid_single_sub = OutputSubScriptGenerator(FceValidSingleGenerateSubScript)
test_single_sub = OutputSubScriptGenerator(FceTestSingleGenerateSubScript)
ensemble_sub = OutputSubScriptGenerator(FceEnsembleGenerateSubScript)

generate_fce_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
generate_fce_test_single = ScriptGenerator(test_single_run, test_single_sub)
generate_fce_ensemble = ScriptGenerator(ensemble_run, ensemble_sub)

