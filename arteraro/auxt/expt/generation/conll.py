from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript

class CoNLL13SourceInterface:
    def get_input_path(self):
        return self.eval_config['conll']['valid_src']

class CoNLL14SourceInterface:
    def get_input_path(self):
        return self.eval_config['conll']['test_src']

class CoNLL13SingleGenerationJobScript(GECSingleGenerationJobScript, CoNLL13SourceInterface):
    pass

class CoNLL14SingleGenerationJobScript(GECSingleGenerationJobScript, CoNLL14SourceInterface):
    pass

class CoNLL13SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_valid.sh'

class CoNLL14SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_test.sh'

class CoNLL13SingleGenerationRunScript(GenerationRunScript, CoNLL13SingleGenerationPathInterface):
    pass

class CoNLL13SingleGenerationSubScript(GenerationSubScript, CoNLL13SingleGenerationPathInterface):
    pass

class CoNLL14SingleGenerationRunScript(GenerationRunScript, CoNLL14SingleGenerationPathInterface):
    pass

class CoNLL14SingleGenerationSubScript(GenerationSubScript, CoNLL14SingleGenerationPathInterface):
    pass

