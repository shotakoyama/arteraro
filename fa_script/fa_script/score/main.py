from fa_script.score.bea19 import score_bea19_valid_single
from fa_script.score.conll import score_conll_valid_single, score_conll_test_single
from fa_script.score.fce import score_fce_valid_single, score_fce_test_single
from fa_script.score.jfleg import score_jfleg_valid_single, score_jfleg_test_single

def valid():
    score_bea19_valid_single()
    score_conll_valid_single()
    score_fce_valid_single()
    score_jfleg_valid_single()

def test():
    score_conll_test_single()
    score_fce_test_single()
    score_jfleg_test_single()

