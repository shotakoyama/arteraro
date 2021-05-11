from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript

class BEA19ValidSingleGenerationJobScript(GECSingleGenerationJobScript):
    def get_input_path(self):
        return self.eval_config['bea19']['valid_src']

class BEA19ValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_valid.sh'

class BEA19ValidSingleGenerationRunScript(GenerationRunScript, BEA19ValidSingleGenerationPathInterface):
    pass

class BEA19ValidSingleGenerationSubScript(GenerationSubScript, BEA19ValidSingleGenerationPathInterface):
    pass

