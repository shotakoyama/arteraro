from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.errant import ErrantResultTable

class BEA19ValidSingleGenerationJobScript(GECSingleGenerationJobScript):
    def get_input_path(self):
        return self.eval_config['bea19']['valid_src']

class BEA19ValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_valid.sh'

class BEA19ValidSingleGenerationRunScript(
        GenerationRunScript,
        BEA19ValidSingleGenerationPathInterface):
    pass

class BEA19ValidSingleGenerationSubScript(
        GenerationSubScript,
        BEA19ValidSingleGenerationPathInterface):
    pass

class BEA19TestSingleGenerationJobScript(GECSingleGenerationJobScript):
    def get_input_path(self):
        return self.eval_config['bea19']['test_src']

class BEA19TestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_test.sh'

class BEA19TestSingleGenerationRunScript(
        GenerationRunScript,
        BEA19TestSingleGenerationPathInterface):
    pass

class BEA19TestSingleGenerationSubScript(
        GenerationSubScript,
        BEA19TestSingleGenerationPathInterface):
    pass

def bea19_valid_generation():
    outdir_list = get_single_valid_outdir_list('bea19')
    script_list = [BEA19ValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            BEA19ValidSingleGenerationRunScript,
            BEA19ValidSingleGenerationSubScript)

def bea19_test_generation():
    valid_result_table = ErrantResultTable('bea19', 'valid')
    outdir_list = get_single_test_outdir_list('bea19', valid_result_table)
    script_list = [BEA19TestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            BEA19TestSingleGenerationRunScript,
            BEA19TestSingleGenerationSubScript)

