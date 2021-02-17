from arteraro.fa_script.result.m2 import M2Result, M2ResultTable, make_ensemble_m2_result, make_rescore_m2_result_list
from arteraro.fa_script.result.show import show_valid_single_results, show_test_single_results, show_ensemble_result, show_valid_rescore_result, show_test_rescore_result

def main():
    print('---CONLL 13 (valid)---')
    show_valid_single_results('conll', M2ResultTable)
    show_ensemble_result('conll', 'valid', make_ensemble_m2_result)
    show_valid_rescore_result('conll', make_rescore_m2_result_list)
    print('---CONLL 14 (test)---')
    show_test_single_results('conll', M2ResultTable, M2Result)
    show_ensemble_result('conll', 'test', make_ensemble_m2_result)
    show_test_rescore_result('conll', make_rescore_m2_result_list, M2Result)

