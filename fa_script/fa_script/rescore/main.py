from fa_script.rescore.bea19 import bea19_rescore_regenerate, bea19_rescore_valid_score
from fa_script.rescore.conll import conll_rescore_regenerate, conll_rescore_valid_score, conll_rescore_test_score
from fa_script.rescore.fce import fce_rescore_regenerate, fce_rescore_valid_score, fce_rescore_test_score
from fa_script.rescore.jfleg import jfleg_rescore_regenerate, jfleg_rescore_valid_score, jfleg_rescore_test_score

def main():
    bea19_rescore_regenerate()
    bea19_rescore_valid_score()

    conll_rescore_regenerate()
    conll_rescore_valid_score()
    conll_rescore_test_score()

    fce_rescore_regenerate()
    fce_rescore_valid_score()
    fce_rescore_test_score()

    jfleg_rescore_regenerate()
    jfleg_rescore_valid_score()
    jfleg_rescore_test_score()

