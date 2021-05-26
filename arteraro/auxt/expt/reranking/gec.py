from .run import RerankingRunScript
from .sub import RerankingSubScript
from .job import RerankingJobScript
from .util import get_arch_list
from arteraro.auxt.util.run import generate_run
from arteraro.auxt.expt.util import get_ensemble_reranking_outdir
from arteraro.auxt.expt.score.errant import (
        bea19_valid_ensemble_reranked_score,
        fce_valid_ensemble_reranked_score,
        fce_test_ensemble_reranked_score)
from arteraro.auxt.expt.score.m2 import (
        conll13_ensemble_reranked_score,
        conll14_ensemble_reranked_score)
from arteraro.auxt.expt.score.gleu import (
        jfleg_valid_ensemble_reranked_score,
        jfleg_test_ensemble_reranked_score)

class BEA19ValidEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_bea19_valid_ensemble.sh'

class BEA19ValidEnsembleRerankingRunScript(
        BEA19ValidEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class BEA19ValidEnsembleRerankingSubScript(
        BEA19ValidEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class BEA19TestEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_bea19_test_ensemble.sh'

class BEA19TestEnsembleRerankingRunScript(
        BEA19TestEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class BEA19TestEnsembleRerankingSubScript(
        BEA19TestEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class CoNLL13EnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_conll_valid_ensemble.sh'

class CoNLL13EnsembleRerankingRunScript(
        CoNLL13EnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class CoNLL13EnsembleRerankingSubScript(
        CoNLL13EnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class CoNLL14EnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_conll_test_ensemble.sh'

class CoNLL14EnsembleRerankingRunScript(
        CoNLL14EnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class CoNLL14EnsembleRerankingSubScript(
        CoNLL14EnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class FCEValidEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_fce_valid_ensemble.sh'

class FCEValidEnsembleRerankingRunScript(
        FCEValidEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class FCEValidEnsembleRerankingSubScript(
        FCEValidEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class FCETestEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_fce_test_ensemble.sh'

class FCETestEnsembleRerankingRunScript(
        FCETestEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class FCETestEnsembleRerankingSubScript(
        FCETestEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class JFLEGValidEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_jfleg_valid_ensemble.sh'

class JFLEGValidEnsembleRerankingRunScript(
        JFLEGValidEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class JFLEGValidEnsembleRerankingSubScript(
        JFLEGValidEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

class JFLEGTestEnsembleRerankingPathInterface:
    def make_path(self):
        return 'rerank_jfleg_test_ensemble.sh'

class JFLEGTestEnsembleRerankingRunScript(
        JFLEGTestEnsembleRerankingPathInterface,
        RerankingRunScript):
    pass

class JFLEGTestEnsembleRerankingSubScript(
        JFLEGTestEnsembleRerankingPathInterface,
        RerankingSubScript):
    pass

def ensemble_reranking(dataset, phase, run_script_class, sub_script_class):
    arch_list = get_arch_list()
    outdir_list = [get_ensemble_reranking_outdir(dataset, phase, arch)
            for arch in arch_list]
    script_list = [RerankingJobScript(outdir) for outdir in outdir_list]
    generate_run(script_list, run_script_class, sub_script_class)

def bea19_valid_ensemble_reranking():
    ensemble_reranking('bea19', 'valid',
            BEA19ValidEnsembleRerankingRunScript,
            BEA19ValidEnsembleRerankingSubScript)

def bea19_test_ensemble_reranking():
    ensemble_reranking('bea19', 'test',
            BEA19TestEnsembleRerankingRunScript,
            BEA19TestEnsembleRerankingSubScript)

def conll_valid_ensemble_reranking():
    ensemble_reranking('conll', 'valid',
            CoNLL13EnsembleRerankingRunScript,
            CoNLL13EnsembleRerankingSubScript)

def conll_test_ensemble_reranking():
    ensemble_reranking('conll', 'test',
            CoNLL14EnsembleRerankingRunScript,
            CoNLL14EnsembleRerankingSubScript)

def fce_valid_ensemble_reranking():
    ensemble_reranking('fce', 'valid',
            FCEValidEnsembleRerankingRunScript,
            FCEValidEnsembleRerankingSubScript)

def fce_test_ensemble_reranking():
    ensemble_reranking('fce', 'test',
            FCETestEnsembleRerankingRunScript,
            FCETestEnsembleRerankingSubScript)

def jfleg_valid_ensemble_reranking():
    ensemble_reranking('jfleg', 'valid',
            JFLEGValidEnsembleRerankingRunScript,
            JFLEGValidEnsembleRerankingSubScript)

def jfleg_test_ensemble_reranking():
    ensemble_reranking('jfleg', 'test',
            JFLEGTestEnsembleRerankingRunScript,
            JFLEGTestEnsembleRerankingSubScript)

def gec_ensemble_reranking(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_ensemble_reranking()
        bea19_test_ensemble_reranking()
        bea19_valid_ensemble_reranked_score()
    if conll:
        conll_valid_ensemble_reranking()
        conll_test_ensemble_reranking()
        conll13_ensemble_reranked_score()
        conll14_ensemble_reranked_score()
    if fce:
        fce_valid_ensemble_reranking()
        fce_test_ensemble_reranking()
        fce_valid_ensemble_reranked_score()
        fce_test_ensemble_reranked_score()
    if jfleg:
        jfleg_valid_ensemble_reranking()
        jfleg_test_ensemble_reranking()
        jfleg_valid_ensemble_reranked_score()
        jfleg_test_ensemble_reranked_score()

