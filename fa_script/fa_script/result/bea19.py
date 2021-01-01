from fa_script.result.errant import ErrantResultTable, make_ensemble_errant_result, make_rescore_errant_result_list
from fa_script.result.show import show_valid_single_results, show_ensemble_result, show_valid_rescore_result

def main():
    print('---BEA19 Valid---')
    show_valid_single_results('bea19', ErrantResultTable)
    show_ensemble_result('bea19', 'valid', make_ensemble_errant_result)
    show_valid_rescore_result('bea19', make_rescore_errant_result_list)

