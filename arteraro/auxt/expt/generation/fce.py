from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.errant import ErrantResultTable

class FCEValidSourceInterface:
    def get_input_path(self):
        return self.eval_config['fce']['valid_src']

class FCETestSourceInterface:
    def get_input_path(self):
        return self.eval_config['fce']['test_src']

class FCEValidSingleGenerationJobScript(
        GECSingleGenerationJobScript,
        FCEValidSourceInterface):
    pass

class FCETestSingleGenerationJobScript(
        GECSingleGenerationJobScript,
        FCETestSourceInterface):
    pass

class FCEValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_valid.sh'

class FCETestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_test.sh'

class FCEValidSingleGenerationRunScript(
        GenerationRunScript,
        FCEValidSingleGenerationPathInterface):
    pass

class FCEValidSingleGenerationSubScript(
        GenerationSubScript,
        FCEValidSingleGenerationPathInterface):
    pass

class FCETestSingleGenerationRunScript(
        GenerationRunScript,
        FCETestSingleGenerationPathInterface):
    pass

class FCETestSingleGenerationSubScript(
        GenerationSubScript,
        FCETestSingleGenerationPathInterface):
    pass

def fce_valid_generation():
    outdir_list = get_single_valid_outdir_list('fce')
    script_list = [FCEValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            FCEValidSingleGenerationRunScript,
            FCEValidSingleGenerationSubScript)

def fce_test_generation():
    valid_result_table = ErrantResultTable('fce', 'valid')
    outdir_list = get_single_test_outdir_list('fce', valid_result_table)
    script_list = [FCETestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            FCETestSingleGenerationRunScript,
            FCETestSingleGenerationSubScript)

