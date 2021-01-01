import numpy as np
from fa_script.util.base import make_base_dir, make_ensemble_base_dir
from fa_script.result.gleu import GleuResult, GleuResultTable, make_ensemble_gleu_result, make_rescore_gleu_result_list

def show_valid_single_results(dataset, result_table_class):
    result_table = result_table_class(dataset, 'valid')
    for index, result_list in enumerate(result_table):
        minimum = min(result_list)
        maximum = max(result_list)
        num_results = len(result_list)
        print('index {} ({}):\tmax {} ({}),\tmin {} ({})'.format(
            index, num_results, maximum.gleu, maximum.epoch, minimum.gleu, minimum.epoch))
    ave = np.mean([max(result_list).gleu for result_list in result_table])
    print('average: {}'.format(ave))

def show_test_single_results(dataset, valid_result_table_class, test_result_class):
    valid_result_table = valid_result_table_class(dataset, 'valid')
    test_result_list = []
    for valid_result in valid_result_table.maximum_list():
        base_dir = make_base_dir(valid_result.index, dataset, 'test', valid_result.epoch)
        result_path = base_dir / 'result.res'
        if result_path.exists():
            test_result = test_result_class(valid_result.index, valid_result.epoch, result_path)
            test_result_list.append(test_result)
            print('index {}: {} ({})'.format(
                test_result.index, test_result.gleu, test_result.epoch))
    if len(test_result_list) > 0:
        ave = np.mean([result.gleu for result in test_result_list])
        print('average: {}'.format(ave))

def show_ensemble_result(dataset, stage, result_fn):
    result = result_fn(dataset, stage)
    if result is not None:
        print('ensemble: {}'.format(result.gleu))

def show_valid_rescore_result(dataset, result_list_fn):
    result_list = result_list_fn(dataset, 'valid')
    if len(result_list) > 0:
        maximum = max(result_list)
        print('rescore (l={}): {}'.format(maximum.l, maximum.gleu))

def show_test_rescore_result(dataset, valid_result_list_fn, test_result_class):
    valid_result_list = valid_result_list_fn(dataset, 'valid')
    if len(valid_result_list) > 0:
        valid_maximum = max(valid_result_list)
        best_l = valid_maximum.l
        best_lmil = int(best_l * 1000)
        result_path = make_ensemble_base_dir(dataset, 'test') / 'result.{}.res'.format(best_lmil)
        test_result = test_result_class(None, None, result_path, l = best_l)
        print('rescore (l={}): {}'.format(test_result.l, test_result.gleu))

def main():
    print('---JFLEG Valid---')
    show_valid_single_results('jfleg', GleuResultTable)
    show_ensemble_result('jfleg', 'valid', make_ensemble_gleu_result)
    show_valid_rescore_result('jfleg', make_rescore_gleu_result_list)
    print('---JFLEG Test---')
    show_test_single_results('jfleg', GleuResultTable, GleuResult)
    show_ensemble_result('jfleg', 'test', make_ensemble_gleu_result)
    show_test_rescore_result('jfleg', make_rescore_gleu_result_list, GleuResult)

