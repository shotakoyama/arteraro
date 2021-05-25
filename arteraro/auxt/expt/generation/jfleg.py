from .run import GenerationRunScript
from .sub import GenerationSubScript
from .gec_job import GECSingleGenerationJobScript
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.gleu import GLEUResultTable

class JFLEGValidSourceInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['valid_src']

class JFLEGTestSourceInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['test_src']

class JFLEGValidSingleGenerationJobScript(
        GECSingleGenerationJobScript,
        JFLEGValidSourceInterface):
    pass

class JFLEGTestSingleGenerationJobScript(
        GECSingleGenerationJobScript,
        JFLEGTestSourceInterface):
    pass

class JFLEGValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_valid.sh'

class JFLEGTestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_test.sh'

class JFLEGValidSingleGenerationRunScript(
        GenerationRunScript,
        JFLEGValidSingleGenerationPathInterface):
    pass

class JFLEGValidSingleGenerationSubScript(
        GenerationSubScript,
        JFLEGValidSingleGenerationPathInterface):
    pass

class JFLEGTestSingleGenerationRunScript(
        GenerationRunScript,
        JFLEGTestSingleGenerationPathInterface):
    pass

class JFLEGTestSingleGenerationSubScript(
        GenerationSubScript,
        JFLEGTestSingleGenerationPathInterface):
    pass

def jfleg_valid_generation():
    outdir_list = get_single_valid_outdir_list('jfleg')
    script_list = [JFLEGValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGValidSingleGenerationRunScript,
            JFLEGValidSingleGenerationSubScript)

def jfleg_test_generation():
    valid_result_table = GLEUResultTable('jfleg', 'valid')
    outdir_list = get_single_test_outdir_list('jfleg', valid_result_table)
    script_list = [JFLEGTestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGTestSingleGenerationRunScript,
            JFLEGTestSingleGenerationSubScript)

