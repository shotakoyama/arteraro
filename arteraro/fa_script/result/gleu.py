from arteraro.fa_script.result.result import (
        Result,
        ResultList,
        ResultTable,
        make_ensemble_result,
        make_rescore_result_list)

class GleuResult(Result):
    def init_attr(self, x):
        self.gleu = float(x[1].split(',')[0].replace("'", '').replace('[', ''))

    def __lt__(self, other):
        return self.gleu < other.gleu

class GleuResultList(ResultList):
    def make_result(self, epoch, output):
        return GleuResult(self.index, epoch, output)

class GleuResultTable(ResultTable):
    def make_result_list(self, index):
        return GleuResultList(self.dataset, self.stage, index)

def make_ensemble_gleu_result(dataset, stage):
    return make_ensemble_result(GleuResult, dataset, stage)

def make_rescore_gleu_result_list(dataset, stage):
    return make_rescore_result_list(GleuResult, dataset, stage)

