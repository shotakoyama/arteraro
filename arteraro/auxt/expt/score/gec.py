from arteraro.auxt.expt.util import get_single_valid_outdir_list
from arteraro.auxt.util.run import generate_run
from .errant import (
        BEA19ValidScoreJobScript,
        BEA19ValidRerankingScoreJobScript,
        FCEValidScoreJobScript,
        FCEValidRerankingScoreJobScript,
        FCETestScoreJobScript,
        FCETestRerankingScoreJobScript,
        BEA19ValidSingleScoreRunScript,
        FCEValidSingleScoreRunScript,
        FCETestSingleScoreRunScript,
        BEA19ValidSingleScoreSubScript,
        FCEValidSingleScoreSubScript,
        FCETestSingleScoreSubScript)
from .m2 import (
        CoNLL13ScoreJobScript,
        CoNLL13RerankingScoreJobScript,
        CoNLL14ScoreJobScript,
        CoNLL14RerankingScoreJobScript,
        CoNLL13SingleScoreRunScript,
        CoNLL14SingleScoreRunScript,
        CoNLL13SingleScoreSubScript,
        CoNLL14SingleScoreSubScript)
from .gleu import (
        JFLEGValidScoreJobScript,
        JFLEGValidRerankingScoreJobScript,
        JFLEGTestScoreJobScript,
        JFLEGTestRerankingScoreJobScript,
        JFLEGValidSingleScoreRunScript,
        JFLEGTestSingleScoreRunScript,
        JFLEGValidSingleScoreSubScript,
        JFLEGTestSingleScoreSubScript)

def bea19_valid_score():
    script_list = [BEA19ValidScoreJobScript(outdir)
            for outdir in get_single_valid_outdir_list('bea19', 'valid')]
    generate_run(script_list,
            BEA19ValidSingleScoreRunScript,
            BEA19ValidSingleScoreSubScript)

def conll13_score():
    script_list = [CoNLL13ScoreJobScript(outdir)
            for outdir in get_single_valid_outdir_list('conll', 'valid')]
    generate_run(script_list,
            CoNLL13SingleScoreRunScript,
            CoNLL13SingleScoreSubScript)

def fce_valid_score():
    script_list = [FCEValidScoreJobScript(outdir)
            for outdir in get_single_valid_outdir_list('fce', 'valid')]
    generate_run(script_list,
            FCEValidSingleScoreRunScript,
            FCEValidSingleScoreSubScript)

def jfleg_valid_score():
    script_list = [JFLEGValidScoreJobScript(outdir)
            for outdir in get_single_valid_outdir_list('jfleg', 'valid')]
    generate_run(script_list,
            JFLEGValidSingleScoreRunScript,
            JFLEGValidSingleScoreSubScript)

def gec_valid_score(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_score()
    if conll:
        conll13_score()
    if fce:
        fce_valid_score()
    if jfleg:
        jfleg_valid_score()

