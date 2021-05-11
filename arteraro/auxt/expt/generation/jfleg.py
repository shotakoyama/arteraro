from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript

class JFLEGValidSourceInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['valid_src']

class JFLEGTestSourceInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['test_src']

class JFLEGValidSingleGenerationJobScript(GECSingleGenerationJobScript, JFLEGValidSourceInterface):
    pass

class JFLEGTestSingleGenerationJobScript(GECSingleGenerationJobScript, JFLEGTestSourceInterface):
    pass

class JFLEGValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_valid.sh'

class JFLEGTestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_test.sh'

class JFLEGValidSingleGenerationRunScript(GenerationRunScript, JFLEGValidSingleGenerationPathInterface):
    pass

class JFLEGValidSingleGenerationSubScript(GenerationSubScript, JFLEGValidSingleGenerationPathInterface):
    pass

class JFLEGTestSingleGenerationRunScript(GenerationRunScript, JFLEGTestSingleGenerationPathInterface):
    pass

class JFLEGTestSingleGenerationSubScript(GenerationSubScript, JFLEGTestSingleGenerationPathInterface):
    pass

