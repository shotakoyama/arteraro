from arteraro.auxt.script import RunScript

class GenerationRunScript(RunScript):
    pass

class ValidGenerationRunScript(GenerationRunScript):
    def make_path(self):
        return 'generate_valid.sh'

class TestGenerationRunScript(GenerationRunScript):
    def make_path(self):
        return 'generate_test.sh'

class EnsembleGenerationRunScript(GenerationRunScript):
    def make_path(self):
        return 'generate_ensemble.sh'

