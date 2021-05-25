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
from arteraro.auxt.expt.result.m2 import M2ResultTableFactory

### CoNLL valid JOB
class CoNLL13InputInterface:
    def get_input_path(self):
        return self.eval_config['conll']['valid_src']

class CoNLL13SingleGenerationJobScript(
        CoNLL13InputInterface,
        GECSingleGenerationJobScript):
    pass

class CoNLL13EnsembleGenerationJobScript(
        CoNLL13InputInterface,
        GECEnsembleGenerationJobScript):
    pass


### CoNLL test JOB
class CoNLL14InputInterface:
    def get_input_path(self):
        return self.eval_config['conll']['test_src']

class CoNLL14SingleGenerationJobScript(
        CoNLL14InputInterface,
        GECSingleGenerationJobScript):
    pass

class CoNLL14EnsembleGenerationJobScript(
        CoNLL14InputInterface,
        GECEnsembleGenerationJobScript):
    pass


### CoNll valid RUN/SUB
class CoNLL13SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_valid.sh'

class CoNLL13SingleGenerationRunScript(
        CoNLL13SingleGenerationPathInterface,
        GenerationRunScript):
    pass

class CoNLL13SingleGenerationSubScript(
        CoNLL13SingleGenerationPathInterface,
        GenerationSubScript):
    pass


### CoNLL test RUN/SUB
class CoNLL14SingleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_test.sh'

class CoNLL14SingleGenerationRunScript(
        CoNLL14SingleGenerationPathInterface,
        GenerationRunScript):
    pass

class CoNLL14SingleGenerationSubScript(
        CoNLL14SingleGenerationPathInterface,
        GenerationSubScript):
    pass


### CoNLL ensemble RUN/SUB
class CoNLLEnsembleGenerationPathInterface:
    def make_path(self):
        return 'generate_conll_ensemble.sh'

class CoNLLEnsembleGenerationRunScript(
        CoNLLEnsembleGenerationPathInterface,
        GenerationRunScript):
    pass

class CoNLLEnsembleGenerationSubScript(
        CoNLLEnsembleGenerationPathInterface,
        EnsembleGenerationSubScript):
    pass


### CoNLL generation commands
def conll13_single_generation():
    outdir_list = get_single_valid_outdir_list('conll')
    script_list = [CoNLL13SingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            CoNLL13SingleGenerationRunScript,
            CoNLL13SingleGenerationSubScript)

def conll14_single_generation():
    valid_result_table = M2ResultTableFactory().make('conll', 'valid')
    outdir_list = get_single_test_outdir_list('conll', valid_result_table)
    script_list = [CoNLL14SingleGenerationJobScript(outdir)
            for outdir in outdir_list]
    generate_run(script_list,
            CoNLL14SingleGenerationRunScript,
            CoNLL14SingleGenerationSubScript)

def conll_ensemble_generation():
    valid_result_table = M2ResultTableFactory().make('conll', 'valid')
    valid_outdir = get_ensemble_outdir('conll', 'valid', valid_result_table)
    test_outdir = get_ensemble_outdir('conll', 'test', valid_result_table)
    script_list = [
            CoNLL13EnsembleGenerationJobScript(valid_outdir),
            CoNLL14EnsembleGenerationJobScript(test_outdir)]
    generate_run(script_list,
            CoNLLEnsembleGenerationRunScript,
            CoNLLEnsembleGenerationSubScript)

