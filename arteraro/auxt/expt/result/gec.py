from arteraro.auxt.expt.result.fscore import FScoreResultList
from arteraro.auxt.expt.result.errant import (
        ErrantResult,
        ErrantResultTableFactory)
from arteraro.auxt.expt.result.m2 import (
        M2Result,
        M2ResultTableFactory)
from arteraro.auxt.expt.result.gleu import (
        GLEUResult,
        GLEUResultList,
        GLEUResultTableFactory)
from arteraro.auxt.expt.util import get_single_test_outdir_list

def test_single_result(dataset, valid_result_table, result_class, result_list_class):
    test_outdir_list = get_single_test_outdir_list(dataset, valid_result_table)
    test_result_list = [result_class(outdir) for outdir in test_outdir_list]
    test_result_list = result_list_class(test_result_list)

    for result in test_result_list:
        line = 'index {} ({}): {}'.format(
                result.outdir.index,
                result.outdir.epoch,
                result.show())
        print(line)
    print(test_result_list.show_avg())


def bea19_result():
    print('----- BEA19 valid -----')
    valid_result_table = ErrantResultTableFactory().make('bea19', 'valid')
    print(valid_result_table.show())


def conll_result():
    print('----- CoNLL 13 (valid) -----')
    valid_result_table = M2ResultTableFactory().make('conll', 'valid')
    print(valid_result_table.show())

    print('\n----- CoNLL 14 (test) -----')
    test_single_result('conll', valid_result_table, M2Result, FScoreResultList)


def fce_result():
    print('----- FCE valid -----')
    valid_result_table = ErrantResultTableFactory().make('fce', 'valid')
    print(valid_result_table.show())

    print('\n----- FCE test -----')
    test_single_result('fce', valid_result_table, ErrantResult, FScoreResultList)


def jfleg_result():
    print('----- JFLEG valid -----')
    valid_result_table = GLEUResultTableFactory().make('jfleg', 'valid')
    print(valid_result_table.show())

    print('\n----- JFLEG test -----')
    test_single_result('jfleg', valid_result_table, GLEUResult, GLEUResultList)

