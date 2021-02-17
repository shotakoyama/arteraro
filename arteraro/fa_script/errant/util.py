import numpy as np
from arteraro.fa_script.util.load import load_config
from arteraro.fa_script.util.prod import make_index_list, make_epoch_list
from arteraro.fa_script.util.base import make_base_dir, make_ensemble_base_dir
from arteraro.fa_script.result.result import Result, ResultList, ResultTable

class ErrorTypeScore:
    def __init__(self, error_type, tp, fp, fn, p, r, f):
        self.error_type = error_type
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)

class ErrantCat2Result(Result):
    error_types = [
            'ADJ', 'ADJ:FORM', 'ADV', 'CONJ', 'CONTR', 'DET',
            'MORPH', 'NOUN', 'NOUN:INFL', 'NOUN:NUM', 'NOUN:POSS', 'ORTH',
            'OTHER', 'PART', 'PREP', 'PRON', 'PUNCT', 'SPELL',
            'VERB', 'VERB:FORM', 'VERB:INFL', 'VERB:SVA', 'VERB:TENSE', 'WO']

    def init_attr(self, lines):
        tp, fp, fn, p, r, f = lines[-3].split('\t')
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)

        self.dct = {error_type: 0.0 for error_type in self.error_types}
        for error_type in self.error_types:
            for line in lines:
                splitted_line = line.split()
                if len(splitted_line) > 0 and splitted_line[0] == error_type:
                    self.dct[error_type] = ErrorTypeScore(*splitted_line)

    def cat_score(self):
        return [self.dct[error_type].f for error_type in self.error_types]

class ErrantCat2ResultList(ResultList):
    def make_result(self, epoch, output):
        return ErrantCat2Result(self.index, epoch, output)

    def make(self):
        for epoch in make_epoch_list(self.config):
            base_dir = make_base_dir(self.index, self.dataset, self.stage, epoch)
            self.add(epoch, base_dir / 'result.cat2')

class ErrantCat2ResultTable(ResultTable):
    def make_result_list(self, index):
        return ErrantCat2ResultList(self.dataset, self.stage, index)

def valid_single_errant_result(dataset):
    tab = ErrantCat2ResultTable(dataset, 'valid')
    lst = [result.cat_score() for result in tab.maximum_list()]
    lst = [np.mean(tup) for tup in zip(*lst)]
    return lst

def test_single_errant_result(dataset):
    valid_tab = ErrantCat2ResultTable(dataset, 'valid')
    test_lst = []
    for valid_result in valid_tab.maximum_list():
        result_path = make_base_dir(valid_result.index, dataset, 'test', valid_result.epoch) / 'result.cat2'
        if result_path.exists():
            test_lst.append(ErrantCat2Result(valid_result.index, valid_result.epoch, result_path))
    lst = [result.cat_score() for result in test_lst]
    lst = [np.mean(tup) for tup in zip(*lst)]
    return lst

def ensemble_errant_result(dataset, stage):
    result_path = make_ensemble_base_dir(dataset, stage) / 'result.cat2'
    if result_path.exists():
        result = ErrantCat2Result(None, None, result_path)
    else:
        result = None
    return result

def valid_rescore_errant_results(dataset):
    config = load_config()
    result_list = []
    for l in config['rescore']['lambda']:
        base_dir = make_ensemble_base_dir(dataset, 'valid')
        lmil = int(l * 1000)
        output = base_dir / 'result.{}.cat2'.format(lmil)
        if output.exists():
            result = ErrantCat2Result(None, None, output, l = l)
            result_list.append(result)
    return result_list

def test_rescore_errant_result(dataset):
    valid_lst = valid_rescore_errant_results(dataset)
    if len(valid_lst) > 0:
        lmil = int(max(valid_lst).l * 1000)
        result_path = make_ensemble_base_dir(dataset, 'test') / 'result.{}.cat2'.format(lmil)
        result = ErrantCat2Result(None, None, result_path)
    else:
        result = None
    return result

