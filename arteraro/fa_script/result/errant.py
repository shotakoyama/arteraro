from arteraro.fa_script.result.result import (
        Result,
        ResultList,
        ResultTable,
        make_ensemble_result,
        make_rescore_result_list)

class ErrantResult(Result):
    def init_attr(self, x):
        tp, fp, fn, p, r, f = x[3].split('\t')
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)

class ErrantResultList(ResultList):
    def make_result(self, epoch, output):
        return ErrantResult(self.index, epoch, output)

class ErrantResultTable(ResultTable):
    def make_result_list(self, index):
        return ErrantResultList(self.dataset, self.stage, index)

def make_ensemble_errant_result(dataset, stage):
    return make_ensemble_result(ErrantResult, dataset, stage)

def make_rescore_errant_result_list(dataset, stage):
    return make_rescore_result_list(ErrantResult, dataset, stage)

