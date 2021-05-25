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

### BEA19 valid JOB
class BEA19ValidGenerationInputInterface:
    def get_input_path(self):
        return self.eval_config['bea19']['valid_src']

class BEA19ValidSingleGenerationJobScript(
        BEA19ValidGenerationInputInterface,
        GECSingleGenerationJobScript):
    pass

class BEA19ValidEnsembleGenerationJobScript(
        BEA19ValidGenerationInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### BEA19 valid RUN/SUB
class BEA19ValidSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_valid.sh'

class BEA19ValidSingleGenerationRunScript(
        BEA19ValidSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class BEA19ValidSingleGenerationSubScript(
        BEA19ValidSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### BEA19 test JOB
class BEA19TestGenerationInputInterface:
    def get_input_path(self):
        return self.eval_config['bea19']['test_src']

class BEA19TestSingleGenerationJobScript(
        BEA19TestGenerationInputInterface,
        GECSingleGenerationJobScript):
    pass

class BEA19TestEnsembleGenerationJobScript(
        BEA19TestGenerationInputInterface,
        GECEnsembleGenerationJobScript):
    pass


### BEA19 test RUN/SUB
class BEA19TestSingleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_test.sh'

class BEA19TestSingleGenerationRunScript(
        BEA19TestSingleGenerationPathInterface,
        GenerationRunScript):
    pass

class BEA19TestSingleGenerationSubScript(
        BEA19TestSingleGenerationPathInterface,
        GenerationSubScript):
    pass


### BEA19 ensemble RUN/SUB
class BEA19EnsembleGenerationPathInterface:
    def make_path(self):
        return 'generate_bea19_ensemble.sh'

class BEA19EnsembleGenerationRunScript(
        BEA19EnsembleGenerationPathInterface,
        GenerationRunScript):
    pass

class BEA19EnsembleGenerationSubScript(
        BEA19EnsembleGenerationPathInterface,
        EnsembleGenerationSubScript):
    pass


### BEA19 generation commands
def bea19_valid_single_generation():
    outdir_list = get_single_valid_outdir_list('bea19')
    script_list = [BEA19ValidSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            BEA19ValidSingleGenerationRunScript,
            BEA19ValidSingleGenerationSubScript)

def bea19_test_single_generation():
    valid_result_table = ErrantResultTableFactory().make('bea19', 'valid')
    outdir_list = get_single_test_outdir_list('bea19', valid_result_table)
    script_list = [BEA19TestSingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            BEA19TestSingleGenerationRunScript,
            BEA19TestSingleGenerationSubScript)

def bea19_ensemble_generation():
    valid_result_table = ErrantResultTableFactory().make('bea19', 'valid')
    valid_outdir = get_ensemble_outdir('bea19', 'valid', valid_result_table)
    test_outdir = get_ensemble_outdir('bea19', 'test', valid_result_table)
    script_list = [
            BEA19ValidEnsembleGenerationJobScript(valid_outdir),
            BEA19TestEnsembleGenerationJobScript(test_outdir)]
    generate_run(script_list,
            BEA19EnsembleGenerationRunScript,
            BEA19EnsembleGenerationSubScript)

