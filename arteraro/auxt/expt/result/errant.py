import numpy as np
from .fscore import (
        FScoreResult,
        FScoreResultListFactory,
        FScoreResultTableFactory)

class ErrantResult(FScoreResult):
    def init_attr(self, x):
        tp, fp, fn, p, r, f = self.read_result()[3].split('\t')
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)


class ErrantResultListFactory(FScoreResultListFactory):
    def make_result(self, outdir):
        return ErrantResult(outdir)


class ErrantResultTableFactory(FScoreResultTableFactory):
    def make_result_list_factory(self):
        return ErrantResultListFactory()

