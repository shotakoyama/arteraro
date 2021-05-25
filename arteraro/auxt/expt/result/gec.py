from arteraro.auxt.expt.result.errant import (
        ErrantResult,
        ErrantResultTable)
from arteraro.auxt.expt.result.m2 import (
        M2Result,
        M2ResultTable)
from arteraro.auxt.expt.result.gleu import (
        GLEUResult,
        GLEUResultTable)
from arteraro.auxt.expt.util import get_single_test_outdir_list

def bea19_result():
    table = ErrantResultTable('bea19', 'valid')
    print(table.show())

def conll_result():
    valid_result_table = M2ResultTable('conll', 'valid')
    print(valid_result_table.show())
    test_outdir_list = get_single_test_outdir_list('conll', valid_result_table)
    test_result_list = [M2Result(outdir) for outdir in test_outdir_list]
    for result in test_result_list:
        line = 'index {} ({}): {}'.format(
                result.outdir.index,
                result.outdir.epoch,
                result.show())
        print(line)


def fce_result():
    table = ErrantResultTable('fce', 'valid')
    print(table.show())

def jfleg_result():
    table = GLEUResultTable('jfleg', 'valid')
    print(table.show())

