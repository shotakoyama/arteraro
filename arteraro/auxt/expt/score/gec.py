from .errant import (
        bea19_valid_single_score,
        fce_valid_single_score,
        fce_test_single_score,
        bea19_valid_ensemble_score,
        fce_valid_ensemble_score,
        fce_test_ensemble_score)
from .m2 import (
        conll13_single_score,
        conll13_ensemble_score,
        conll14_single_score,
        conll14_ensemble_score)
from .gleu import (
        jfleg_valid_single_score,
        jfleg_valid_ensemble_score,
        jfleg_test_single_score,
        jfleg_test_ensemble_score)

def gec_valid_score(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_single_score()
    if conll:
        conll13_single_score()
    if fce:
        fce_valid_single_score()
    if jfleg:
        jfleg_valid_single_score()

def gec_test_score(conll, fce, jfleg):
    if conll:
        conll14_single_score()
    if fce:
        fce_test_single_score()
    if jfleg:
        jfleg_test_single_score()

def gec_ensemble_score(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_ensemble_score()
    if conll:
        conll13_ensemble_score()
        conll14_ensemble_score()
    if fce:
        fce_valid_ensemble_score()
        fce_test_ensemble_score()
    if jfleg:
        jfleg_valid_ensemble_score()
        jfleg_test_ensemble_score()

