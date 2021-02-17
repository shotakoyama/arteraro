from arteraro.fa_script.generate.bea19 import generate_bea19_ensemble
from arteraro.fa_script.score.bea19 import score_bea19_valid_ensemble
from arteraro.fa_script.generate.conll import generate_conll_ensemble
from arteraro.fa_script.score.conll import score_conll_valid_ensemble, score_conll_test_ensemble
from arteraro.fa_script.generate.fce import generate_fce_ensemble
from arteraro.fa_script.score.fce import score_fce_valid_ensemble, score_fce_test_ensemble
from arteraro.fa_script.generate.jfleg import generate_jfleg_ensemble
from arteraro.fa_script.score.jfleg import score_jfleg_valid_ensemble, score_jfleg_test_ensemble
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('-b', '--bea19', action='store_true')
    parser.add_argument('-c', '--conll', action='store_true')
    parser.add_argument('-f', '--fce', action='store_true')
    args = parser.parse_args()

    if not (args.conll or args.fce):
        generate_bea19_ensemble()
        score_bea19_valid_ensemble()

    if not (args.bea19 or args.fce):
        generate_conll_ensemble()
        score_conll_valid_ensemble()
        score_conll_test_ensemble()

    if not (args.bea19 or args.conll):
        generate_fce_ensemble()
        score_fce_valid_ensemble()
        score_fce_test_ensemble()

    if not (args.bea19 or args.conll or args.fce):
        generate_jfleg_ensemble()
        score_jfleg_valid_ensemble()
        score_jfleg_test_ensemble()

