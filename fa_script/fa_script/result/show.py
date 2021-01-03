import numpy as np
from fa_script.util.base import make_base_dir, make_ensemble_base_dir

def table_average_score(result_table):
    p = np.mean([max(result_list).p for result_list in result_table])
    r = np.mean([max(result_list).r for result_list in result_table])
    f = np.mean([max(result_list).f for result_list in result_table])
    return p, r, f

def list_average_score(result_list):
    p = np.mean([result.p for result in result_list])
    r = np.mean([result.r for result in result_list])
    f = np.mean([result.f for result in result_list])
    return p, r, f

def show_valid_single_results(dataset, result_table_class):
    result_table = result_table_class(dataset, 'valid')
    for index, result_list in enumerate(result_table):
        minimum = min(result_list)
        maximum = max(result_list)
        num_results = len(result_list)
        print('index {} ({}):\tmax {} ({}, {}, {}),\tmin {} ({}, {}, {})'.format(
            index, num_results,
            maximum.f, maximum.p, maximum.r, maximum.epoch,
            minimum.f, minimum.p, minimum.r, minimum.epoch))
    ave_p, ave_r, ave_f = table_average_score(result_table)
    print('average: {} ({}, {})'.format(ave_f, ave_p, ave_r))

def show_test_single_results(dataset, valid_result_table_class, test_result_class):
    valid_result_table = valid_result_table_class(dataset, 'valid')
    test_result_list = []
    for valid_result in valid_result_table.maximum_list():
        base_dir = make_base_dir(valid_result.index, dataset, 'test', valid_result.epoch)
        result_path = base_dir / 'result.res'
        if result_path.exists():
            try:
                test_result = test_result_class(valid_result.index, valid_result.epoch, result_path)
                test_result_list.append(test_result)
                print('index {}: {} ({}, {}, {})'.format(test_result.index,
                    test_result.f, test_result.p, test_result.r, test_result.epoch))
            except IndexError:
                pass
    if len(test_result_list) > 0:
        ave_p, ave_r, ave_f = list_average_score(test_result_list)
        print('average: {} ({}, {})'.format(ave_f, ave_p, ave_r))

def show_ensemble_result(dataset, stage, result_fn):
    result = result_fn(dataset, stage)
    if result is not None:
        print('ensemble: {} ({}, {})'.format(result.f, result.p, result.r))

def show_valid_rescore_result(dataset, result_list_fn):
    result_list = result_list_fn(dataset, 'valid')
    if len(result_list) > 0:
        maximum = max(result_list)
        print('rescore({}) (l={}): {} ({}, {})'.format(len(result_list), maximum.l, maximum.f, maximum.p, maximum.r))

def show_test_rescore_result(dataset, valid_result_list_fn, test_result_class):
    valid_result_list = valid_result_list_fn(dataset, 'valid')
    if len(valid_result_list) > 0:
        valid_maximum = max(valid_result_list)
        best_l = valid_maximum.l
        best_lmil = int(best_l * 1000)
        result_path = make_ensemble_base_dir(dataset, 'test') / 'result.{}.res'.format(best_lmil)
        test_result = test_result_class(None, None, result_path, l = best_l)
        print('rescore({}) (l={}): {} ({}, {})'.format(
            len(valid_result_list),
            test_result.l,
            test_result.f, test_result.p, test_result.r))

