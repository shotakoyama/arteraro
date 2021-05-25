import numpy as np
from .fscore import (
        FScoreResult,
        FScoreResultListFactory,
        FScoreResultTableFactory)

class M2Result(FScoreResult):
    def init_attr(self, x):
        self.p = float(x[0].split(':')[-1].strip())
        self.r = float(x[1].split(':')[-1].strip())
        self.f = float(x[2].split(':')[-1].strip())


class M2ResultListFactory(FScoreResultListFactory):
    def make_result(self, outdir):
        return M2Result(outdir)


class M2ResultTableFactory(FScoreResultTableFactory):
    def make_result_list_factory(self):
        return M2ResultListFactory()

