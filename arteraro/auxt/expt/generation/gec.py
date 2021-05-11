from arteraro.auxt.expt.util import get_single_valid_outdir_list
from arteraro.auxt.util.run import generate_run
from .bea19 import (
        BEA19ValidSingleGenerationJobScript,
        BEA19ValidSingleGenerationRunScript,
        BEA19ValidSingleGenerationSubScript)
from .conll import (
        CoNLL13SingleGenerationJobScript,
        CoNLL14SingleGenerationJobScript,
        CoNLL13SingleGenerationRunScript,
        CoNLL14SingleGenerationRunScript,
        CoNLL13SingleGenerationSubScript,
        CoNLL14SingleGenerationSubScript)
from .fce import (
        FCEValidSingleGenerationJobScript,
        FCETestSingleGenerationJobScript,
        FCEValidSingleGenerationRunScript,
        FCETestSingleGenerationRunScript,
        FCEValidSingleGenerationSubScript,
        FCETestSingleGenerationSubScript)
from .jfleg import (
        JFLEGValidSingleGenerationJobScript,
        JFLEGTestSingleGenerationJobScript,
        JFLEGValidSingleGenerationRunScript,
        JFLEGTestSingleGenerationRunScript,
        JFLEGValidSingleGenerationSubScript,
        JFLEGTestSingleGenerationSubScript)

def bea19_valid_generation():
    script_list = [BEA19ValidSingleGenerationJobScript(outdir)
            for outdir in get_single_valid_outdir_list('bea19', 'valid')]
    generate_run(script_list,
            BEA19ValidSingleGenerationRunScript,
            BEA19ValidSingleGenerationSubScript)

def conll13_generation():
    script_list = [CoNLL13SingleGenerationJobScript(outdir)
            for outdir in get_single_valid_outdir_list('conll', 'valid')]
    generate_run(script_list,
            CoNLL13SingleGenerationRunScript,
            CoNLL13SingleGenerationSubScript)

def fce_valid_generation():
    script_list = [FCEValidSingleGenerationJobScript(outdir)
            for outdir in get_single_valid_outdir_list('fce', 'valid')]
    generate_run(script_list,
            FCEValidSingleGenerationRunScript,
            FCEValidSingleGenerationSubScript)

def jfleg_valid_generation():
    script_list = [JFLEGValidSingleGenerationJobScript(outdir)
            for outdir in get_single_valid_outdir_list('jfleg', 'valid')]
    generate_run(script_list,
            JFLEGValidSingleGenerationRunScript,
            JFLEGValidSingleGenerationSubScript)

def gec_valid_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_generation()
    if conll:
        conll13_generation()
    if fce:
        fce_valid_generation()
    if jfleg:
        jfleg_valid_generation()

