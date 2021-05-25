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
from arteraro.auxt.expt.result.errant import ErrantResultTableFactory

### FCE valid JOB
class FCEValidInputInterface:
    def get_input_path(self):
        return self.eval_config['fce']['valid_src']

class FCEValidSingleGenerationJobScript(
        FCEValidInputInterface,
        GECSingleGenerationJobScript):
    pass

class FCEValidEnsembleGenerationJobScript(
        FCEValidInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### FCE test JOB
class FCETestInputInterface:
    def get_input_path(self):
        return self.eval_config['fce']['test_src']

class FCETestSingleGenerationJobScript(
        FCETestInputInterface,
        GECSingleGenerationJobScript):
    pass

class FCETestEnsembleGenerationJobScript(
        FCETestInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### FCE valid RUN/SUB
class FCEValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_valid.sh'

class FCEValidSingleGenerationRunScript(
        FCEValidSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class FCEValidSingleGenerationSubScript(
        FCEValidSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### FCE test RUN/SUB
class FCETestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_test.sh'

class FCETestSingleGenerationRunScript(
        FCETestSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class FCETestSingleGenerationSubScript(
        FCETestSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### FCE ensemble RUN/SUB
class FCEEnsembleGenerationPathInterface:
    def make_path(self):
        return 'generate_fce_ensemble.sh'

class FCEEnsembleGenerationRunScript(
        FCEEnsembleGenerationPathInterface,
        GenerationRunScript):
    pass

class FCEEnsembleGenerationSubScript(
        FCEEnsembleGenerationPathInterface,
        EnsembleGenerationSubScript):
    pass


### FCE generation commansd
def fce_valid_single_generation():
    outdir_list = get_single_valid_outdir_list('fce')
    script_list = [FCEValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            FCEValidSingleGenerationRunScript,
            FCEValidSingleGenerationSubScript)

def fce_test_single_generation():
    valid_result_table = ErrantResultTableFactory().make('fce', 'valid')
    outdir_list = get_single_test_outdir_list('fce', valid_result_table)
    script_list = [FCETestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            FCETestSingleGenerationRunScript,
            FCETestSingleGenerationSubScript)

def fce_ensemble_generation():
    valid_result_table = ErrantResultTableFactory().make('fce', 'valid')
    valid_outdir = get_ensemble_outdir('fce', 'valid', valid_result_table)
    test_outdir = get_ensemble_outdir('fce', 'test', valid_result_table)
    script_list = [
            FCEValidEnsembleGenerationJobScript(valid_outdir),
            FCETestEnsembleGenerationJobScript(test_outdir)]
    generate_run(script_list,
            FCEEnsembleGenerationRunScript,
            FCEEnsembleGenerationSubScript)

