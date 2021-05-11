from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript

class FCEValidSourceInterface:
    def get_input_path(self):
        return self.eval_config['fce']['valid_src']

class FCETestSourceInterface:
    def get_input_path(self):
        return self.eval_config['fce']['test_src']

class FCEValidSingleGenerationJobScript(GECSingleGenerationJobScript, FCEValidSourceInterface):
    pass

class FCETestSingleGenerationJobScript(GECSingleGenerationJobScript, FCETestSourceInterface):
    pass

class FCEValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_valid.sh'

class FCETestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_test.sh'

class FCEValidSingleGenerationRunScript(GenerationRunScript, FCEValidSingleGenerationPathInterface):
    pass

class FCEValidSingleGenerationSubScript(GenerationSubScript, FCEValidSingleGenerationPathInterface):
    pass

class FCETestSingleGenerationRunScript(GenerationRunScript, FCETestSingleGenerationPathInterface):
    pass

class FCETestSingleGenerationSubScript(GenerationSubScript, FCETestSingleGenerationPathInterface):
    pass

