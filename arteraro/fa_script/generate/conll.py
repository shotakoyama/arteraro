from arteraro.fa_script.generate.generator import (
        ValidSingleGenerateRunScriptGenerator,
        TestSingleGenerateRunScriptGenerator,
        EnsembleGenerateRunScriptGenerator)
from arteraro.fa_script.generate.run import GenerateRunScript
from arteraro.fa_script.generate.sub import (
        ValidSingleGenerateSubScript,
        TestSingleGenerateSubScript,
        EnsembleGenerateSubScript)
from arteraro.fa_script.result.m2 import M2ResultTable
from arteraro.fa_script.util.output import OutputSubScriptGenerator
from arteraro.fa_script.util.generator import ScriptGenerator

class Conll13SingleGenerateRunScriptGenerator(ValidSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', GenerateRunScript)
        self.buffer_size = 1381
        self.source = self.eval_config['conll']['valid_src']

class Conll14SingleGenerateRunScriptGenerator(TestSingleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', GenerateRunScript)
        self.buffer_size = 1312
        self.source = self.eval_config['conll']['test_src']

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

class ConllEnsembleGenerateRunScriptGenerator(EnsembleGenerateRunScriptGenerator):
    def __init__(self):
        super().__init__('conll', GenerateRunScript)
        self.valid_buffer_size = 1381
        self.test_buffer_size = 1312
        self.valid_source = self.eval_config['conll']['valid_src']
        self.test_source = self.eval_config['conll']['test_src']

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

valid_single_run = Conll13SingleGenerateRunScriptGenerator()
test_single_run = Conll14SingleGenerateRunScriptGenerator()
ensemble_run = ConllEnsembleGenerateRunScriptGenerator()

class Conll13SingleGenerateSubScript(ValidSingleGenerateSubScript):
    def __init__(self):
        super().__init__('conll')

class Conll14SingleGenerateSubScript(TestSingleGenerateSubScript):
    def __init__(self):
        super().__init__('conll')

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

class ConllEnsembleGenerateSubScript(EnsembleGenerateSubScript):
    def __init__(self):
        super().__init__('conll')

    def make_result_table(self):
        return M2ResultTable(self.dataset, 'valid')

valid_single_sub = OutputSubScriptGenerator(Conll13SingleGenerateSubScript)
test_single_sub = OutputSubScriptGenerator(Conll14SingleGenerateSubScript)
ensemble_sub = OutputSubScriptGenerator(ConllEnsembleGenerateSubScript)

generate_conll_valid_single = ScriptGenerator(valid_single_run, valid_single_sub)
generate_conll_test_single = ScriptGenerator(test_single_run, test_single_sub)
generate_conll_ensemble = ScriptGenerator(ensemble_run, ensemble_sub)

