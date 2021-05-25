from .run import GenerationRunScript
from .sub import (
        GenerationSubScript,
        EnsembleGenerationSubScript)
from .gec_job import (
        GECSingleGenerationJobScript,
        GECEnsembleGenerationJobScript)
from arteraro.auxt.expt.util import (
        get_single_valid_outdir_list,
        get_single_test_outdir_list,
        get_ensemble_outdir)
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.result.gleu import GLEUResultTableFactory

### JFLEG valid JOB
class JFLEGValidInputInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['valid_src']

class JFLEGValidSingleGenerationJobScript(
        JFLEGValidInputInterface,
        GECSingleGenerationJobScript):
    pass

class JFLEGValidEnsembleGenerationJobScript(
        JFLEGValidInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### JFLEG test JOB
class JFLEGTestInputInterface:
    def get_input_path(self):
        return self.eval_config['jfleg']['test_src']

class JFLEGTestSingleGenerationJobScript(
        JFLEGTestInputInterface,
        GECSingleGenerationJobScript):
    pass

class JFLEGTestEnsembleGenerationJobScript(
        JFLEGTestInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### JFLEG valid RUN/SUB
class JFLEGValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_valid.sh'

class JFLEGValidSingleGenerationRunScript(
        JFLEGValidSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class JFLEGValidSingleGenerationSubScript(
        JFLEGValidSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### JFLEG test RUN/SUB
class JFLEGTestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_test.sh'

class JFLEGTestSingleGenerationRunScript(
        JFLEGTestSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class JFLEGTestSingleGenerationSubScript(
        JFLEGTestSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### JFLEG ensemble RUN/SUB
class JFLEGEnsembleGenerationPathInterface:
    def make_path(self):
        return 'generate_jfleg_ensemble.sh'

class JFLEGEnsembleGenerationRunScript(
        JFLEGEnsembleGenerationPathInterface,
        GenerationRunScript):
    pass

class JFLEGEnsembleGenerationSubScript(
        JFLEGEnsembleGenerationPathInterface,
        EnsembleGenerationSubScript):
    pass


### JFLEG generation command
def jfleg_valid_single_generation():
    outdir_list = get_single_valid_outdir_list('jfleg')
    script_list = [JFLEGValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGValidSingleGenerationRunScript,
            JFLEGValidSingleGenerationSubScript)

def jfleg_test_single_generation():
    valid_result_table = GLEUResultTableFactory().make('jfleg', 'valid')
    outdir_list = get_single_test_outdir_list('jfleg', valid_result_table)
    script_list = [JFLEGTestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            JFLEGTestSingleGenerationRunScript,
            JFLEGTestSingleGenerationSubScript)

def jfleg_ensemble_generation():
    valid_result_table = GLEUResultTableFactory().make('jfleg', 'valid')
    valid_outdir = get_ensemble_outdir('jfleg', 'valid', valid_result_table)
    test_outdir = get_ensemble_outdir('jfleg', 'test', valid_result_table)
    script_list = [
            JFLEGValidEnsembleGenerationJobScript(valid_outdir),
            JFLEGTestEnsembleGenerationJobScript(test_outdir)]
    generate_run(script_list,
            JFLEGEnsembleGenerationRunScript,
            JFLEGEnsembleGenerationSubScript)

