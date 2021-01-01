from fa_script.result.result import (
        Result,
        ResultList,
        ResultTable,
        make_ensemble_result,
        make_rescore_result_list)

class M2Result(Result):
    def init_attr(self, x):
        self.p = float(x[0].split(':')[-1].strip())
        self.r = float(x[1].split(':')[-1].strip())
        self.f = float(x[2].split(':')[-1].strip())

class M2ResultList(ResultList):
    def make_result(self, epoch, output):
        return M2Result(self.index, epoch, output)

class M2ResultTable(ResultTable):
    def make_result_list(self, index):
        return M2ResultList(self.dataset, self.stage, index)

def make_ensemble_m2_result(dataset, stage):
    return make_ensemble_result(M2Result, dataset, stage)

def make_rescore_m2_result_list(dataset, stage):
    return make_rescore_result_list(M2Result, dataset, stage)

