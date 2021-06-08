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
from arteraro.auxt.expt.util import (
        get_single_test_outdir_list,
        get_ensemble_outdir,
        get_ensemble_reranking_outdir)
from arteraro.auxt.expt.reranking.util import (
        get_arch_list,
        get_lambda_list)

def show_test_single_result(dataset, valid_result_table,
        result_class, result_list_class):
    test_outdir_list = get_single_test_outdir_list(dataset, valid_result_table)
    test_result_list = result_list_class()
    for outdir in test_outdir_list:
        try:
            result = result_class(outdir)
            test_result_list.append(result)
        except FileNotFoundError:
            pass

    if test_result_list:
        for result in test_result_list:
            line = 'index {} ({}): {}'.format(
                    result.outdir.index,
                    result.outdir.epoch,
                    result.show())
            print(line)
        print(test_result_list.show_avg())

def show_ensemble_result(dataset, phase, result_class):
    outdir = get_ensemble_outdir(dataset, phase)
    try:
        result = result_class(outdir)
        print('ensemble: {}'.format(result.show()))
    except FileNotFoundError:
        pass

def show_valid_ensemble_result(dataset, result_class):
    show_ensemble_result(dataset, 'valid', result_class)

def show_test_ensemble_result(dataset, result_class):
    show_ensemble_result(dataset, 'test', result_class)

def show_valid_reranking_result(dataset, result_class,
        result_list_class):
    arch_list = get_arch_list()
    lambda_list = get_lambda_list()
    best_lambda_list = []

    for arch in arch_list:
        result_list = result_list_class()
        outdir = get_ensemble_reranking_outdir(dataset, 'valid', arch)
        for l in lambda_list:
            try:
                lmil = int(l * 1000)
                filename = 'result.{}.txt'.format(lmil)
                result = result_class(outdir, filename = filename, l = l)
                result_list.append(result)
            except FileNotFoundError:
                pass
        if result_list:
            best_lambda = max(result_list).l
            line = 'rerank ({}, l={}, {}):\t{}'.format(arch, best_lambda, len(result_list), result_list.show_best())
            print(line)
            best_lambda_list.append((arch, best_lambda))

    return best_lambda_list

def show_test_reranking_result(dataset, result_class, best_lambda_list):
    for arch, l in best_lambda_list:
        outdir = get_ensemble_reranking_outdir(dataset, 'test', arch)
        try:
            lmil = int(l * 1000)
            filename = 'result.{}.txt'.format(lmil)
            result = result_class(outdir, filename = filename, l = l)
            line = 'rerank ({}, l={}):\t{}'.format(arch, l, result.show())
            print(line)
        except FileNotFoundError:
            pass


def bea19_result():
    print('----- BEA19 valid -----')
    valid_result_table = ErrantResultTableFactory().make('bea19', 'valid')
    print(valid_result_table.show())
    show_valid_ensemble_result('bea19', ErrantResult)
    show_valid_reranking_result('bea19', ErrantResult, FScoreResultList)


def conll_result():
    print('----- CoNLL 13 (valid) -----')
    valid_result_table = M2ResultTableFactory().make('conll', 'valid')
    print(valid_result_table.show())
    show_valid_ensemble_result('conll', M2Result)
    best_lambda_list = show_valid_reranking_result('conll',
            M2Result, FScoreResultList)

    print('\n----- CoNLL 14 (test) -----')
    show_test_single_result('conll', valid_result_table,
            M2Result, FScoreResultList)
    show_test_ensemble_result('conll', M2Result)
    show_test_reranking_result('conll', M2Result, best_lambda_list)


def fce_result():
    print('----- FCE valid -----')
    valid_result_table = ErrantResultTableFactory().make('fce', 'valid')
    print(valid_result_table.show())
    show_valid_ensemble_result('fce', ErrantResult)
    best_lambda_list = show_valid_reranking_result('fce',
            ErrantResult, FScoreResultList)

    print('\n----- FCE test -----')
    show_test_single_result('fce', valid_result_table,
            ErrantResult, FScoreResultList)
    show_test_ensemble_result('fce', ErrantResult)
    show_test_reranking_result('fce', ErrantResult, best_lambda_list)


def jfleg_result():
    print('----- JFLEG valid -----')
    valid_result_table = GLEUResultTableFactory().make('jfleg', 'valid')
    print(valid_result_table.show())
    show_valid_ensemble_result('jfleg', GLEUResult)
    best_lambda_list = show_valid_reranking_result('jfleg',
            GLEUResult, GLEUResultList)

    print('\n----- JFLEG test -----')
    show_test_single_result('jfleg', valid_result_table,
            GLEUResult, GLEUResultList)
    show_test_ensemble_result('jfleg', GLEUResult)
    show_test_reranking_result('jfleg', GLEUResult, best_lambda_list)

