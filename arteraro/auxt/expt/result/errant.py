import numpy as np
from arteraro.auxt.expt.outdir import SinglePhaseDir
from .result import (
        Result,
        ResultList,
        ResultTable)

class ErrantResult(Result):
    def get_result_path(self):
        return self.outdir.make_path('result.txt')

    def init_attr(self, x):
        tp, fp, fn, p, r, f = self.read_result()[3].split('\t')
        self.tp = int(tp)
        self.fp = int(fp)
        self.fn = int(fn)
        self.p = float(p)
        self.r = float(r)
        self.f = float(f)

    def show(self):
        return '{} ({}, {})'.format(self.f, self.p, self.r)

    def __lt__(self, other):
        return self.f < other.f


class ErrantResultList(ResultList):
    def make_result(self, epoch):
        outdir = self.phasedir.make_outdir(epoch)
        return ErrantResult(outdir)

    def show(self):
        num_results = len(self)
        minimum = min(self)
        maximum = max(self)
        lst = ['index {} ({}):'.format(self.phasedir.index, num_results),
            'max {} ({}), ({}, {}),'.format(maximum.f,
                maximum.outdir.epoch, maximum.p, maximum.r),
            'min {} ({}), ({}, {})'.format(minimum.f,
                minimum.outdir.epoch, minimum.p, minimum.r)]
        line = '\t'.join(lst)
        return line


class ErrantResultTable(ResultTable):
    def make_result_list(self, index):
        phasedir = SinglePhaseDir(index, self.dataset, self.phase)
        return ErrantResultList(phasedir)

    def show(self):
        xs = [result_list.show() for result_list in self]

        max_list = self.maximum_list()
        ave_p = np.mean([x.p for x in max_list])
        ave_r = np.mean([x.r for x in max_list])
        ave_f = np.mean([x.f for x in max_list])
        line = 'average: {} ({}, {})'.format(ave_f, ave_p, ave_r)
        xs.append(line)

        return '\n'.join(xs)

