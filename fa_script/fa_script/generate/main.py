from fa_script.generate.bea19 import generate_bea19_valid_single, generate_bea19_test_single
from fa_script.generate.conll import generate_conll_valid_single, generate_conll_test_single
from fa_script.generate.fce import generate_fce_valid_single, generate_fce_test_single
from fa_script.generate.jfleg import generate_jfleg_valid_single, generate_jfleg_test_single

def valid():
    generate_bea19_valid_single()
    generate_conll_valid_single()
    generate_fce_valid_single()
    generate_jfleg_valid_single()

def test():
    generate_bea19_test_single()
    generate_conll_test_single()
    generate_fce_test_single()
    generate_jfleg_test_single()

