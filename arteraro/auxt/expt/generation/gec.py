from .bea19 import (
        bea19_valid_single_generation,
        bea19_test_single_generation,
        bea19_ensemble_generation)
from .conll import (
        conll13_single_generation,
        conll14_single_generation,
        conll_ensemble_generation)
from .fce import (
        fce_valid_single_generation,
        fce_test_single_generation,
        fce_ensemble_generation)
from .jfleg import (
        jfleg_valid_single_generation,
        jfleg_test_single_generation,
        jfleg_ensemble_generation)

def gec_valid_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_valid_single_generation()
    if conll:
        conll13_single_generation()
    if fce:
        fce_valid_single_generation()
    if jfleg:
        jfleg_valid_single_generation()

def gec_test_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_test_single_generation()
    if conll:
        conll14_single_generation()
    if fce:
        fce_test_single_generation()
    if jfleg:
        jfleg_test_single_generation()

def gec_ensemble_generation(bea19, conll, fce, jfleg):
    if bea19:
        bea19_ensemble_generation()
    if conll:
        conll_ensemble_generation()
    if fce:
        fce_ensemble_generation()
    if jfleg:
        jfleg_ensemble_generation()

