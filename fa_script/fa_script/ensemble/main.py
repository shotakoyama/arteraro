from fa_script.generate.bea19 import generate_bea19_ensemble
from fa_script.score.bea19 import score_bea19_valid_ensemble
from fa_script.generate.conll import generate_conll_ensemble
from fa_script.score.conll import score_conll_valid_ensemble, score_conll_test_ensemble
from fa_script.generate.fce import generate_fce_ensemble
from fa_script.score.fce import score_fce_valid_ensemble, score_fce_test_ensemble
from fa_script.generate.jfleg import generate_jfleg_ensemble
from fa_script.score.jfleg import score_jfleg_valid_ensemble, score_jfleg_test_ensemble

def main():
    generate_bea19_ensemble()
    score_bea19_valid_ensemble()

    generate_conll_ensemble()
    score_conll_valid_ensemble()
    score_conll_test_ensemble()

    generate_fce_ensemble()
    score_fce_valid_ensemble()
    score_fce_test_ensemble()

    generate_jfleg_ensemble()
    score_jfleg_valid_ensemble()
    score_jfleg_test_ensemble()

