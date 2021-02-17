from arteraro.fa_script.result.errant import ErrantResult, ErrantResultTable, make_ensemble_errant_result, make_rescore_errant_result_list
from arteraro.fa_script.result.show import show_valid_single_results, show_test_single_results, show_ensemble_result, show_valid_rescore_result, show_test_rescore_result

def main():
    print('---FCE Valid---')
    show_valid_single_results('fce', ErrantResultTable)
    show_ensemble_result('fce', 'valid', make_ensemble_errant_result)
    show_valid_rescore_result('fce', make_rescore_errant_result_list)
    print('---FCE Test---')
    show_test_single_results('fce', ErrantResultTable, ErrantResult)
    show_ensemble_result('fce', 'test', make_ensemble_errant_result)
    show_test_rescore_result('fce', make_rescore_errant_result_list, ErrantResult)

