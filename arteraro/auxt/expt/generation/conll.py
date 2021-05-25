from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.m2 import M2ResultTable

class CoNLL13SourceInterface:
    def get_input_path(self):
        return self.eval_config['conll']['valid_src']

class CoNLL14SourceInterface:
    def get_input_path(self):
        return self.eval_config['conll']['test_src']

class CoNLL13SingleGenerationJobScript(
        GECSingleGenerationJobScript,
        CoNLL13SourceInterface):
    pass

class CoNLL14SingleGenerationJobScript(
        GECSingleGenerationJobScript,
        CoNLL14SourceInterface):
    pass

class CoNLL13SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_valid.sh'

class CoNLL14SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_test.sh'

class CoNLL13SingleGenerationRunScript(
        GenerationRunScript,
        CoNLL13SingleGenerationPathInterface):
    pass

class CoNLL13SingleGenerationSubScript(
        GenerationSubScript,
        CoNLL13SingleGenerationPathInterface):
    pass

class CoNLL14SingleGenerationRunScript(
        GenerationRunScript,
        CoNLL14SingleGenerationPathInterface):
    pass

class CoNLL14SingleGenerationSubScript(
        GenerationSubScript,
        CoNLL14SingleGenerationPathInterface):
    pass

def conll13_generation():
    outdir_list = get_single_valid_outdir_list('conll')
    script_list = [CoNLL13SingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            CoNLL13SingleGenerationRunScript,
            CoNLL13SingleGenerationSubScript)

def conll14_generation():
    valid_result_table = M2ResultTable('conll', 'valid')
    outdir_list = get_single_test_outdir_list('conll', valid_result_table)
    script_list = [CoNLL14SingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            CoNLL14SingleGenerationRunScript,
            CoNLL14SingleGenerationSubScript)

