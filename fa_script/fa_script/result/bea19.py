import numpy as np
from fa_script.util.load import load_config
from fa_script.result.errant import M2ResultTable, make_ensemble_result, make_rescore_results

def show_valid_single_results(config):
    result_table = M2ResultTable(config, 'bea19', 'valid')
    indices = range(len(config['seed_list']))
    for index, result_list in enumerate(result_table):
        minimum = min(result_list)
        maximum = max(result_list)
        result_length = len(result_list)
        print('index {} ({}):\tmax {} ({}, {}, {}),\tmin {} ({}, {}, {})'.format(
            index, result_length,
            maximum.f, maximum.p, maximum.r, maximum.epoch,
            minimum.f, minimum.p, minimum.r, minimum.epoch))

    ave_f = np.mean([max(result_list).f for result_list in result_table])
    ave_p = np.mean([max(result_list).p for result_list in result_table])
    ave_r = np.mean([max(result_list).r for result_list in result_table])
    print('average: {} ({}, {})'.format(ave_f, ave_p, ave_r))

def show_valid_ensemble_results():
    result = make_ensemble_result('bea19', 'valid')
    if result is not None:
        print('ensemble: {} ({}, {})'.format(result.f, result.p, result.r))

def show_valid_rescore_results():
    result_list = make_rescore_results('bea19', 'valid')
    if len(result_list) > 0:
        print('rescore')
        for result in result_list:
            print('l {}: {} ({}, {})'.format(result.l, result.f, result.p, result.r))
        maximum = max(result_list)
        print('max l={}: {} ({}, {})'.format(maximum.l, maximum.f, maximum.p, maximum.r))

def main():
    config = load_config()
    show_valid_single_results(config)
    show_valid_ensemble_results()
    show_valid_rescore_results()

