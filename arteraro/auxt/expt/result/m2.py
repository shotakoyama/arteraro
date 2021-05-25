import numpy as np
from arteraro.auxt.expt.outdir import SinglePhaseDir
from .result import (
        Result,
        ResultList,
        ResultTable)

class M2Result(Result):
    def get_result_path(self):
        return self.outdir.make_path('result.txt')

    def init_attr(self, x):
        self.p = float(x[0].split(':')[-1].strip())
        self.r = float(x[1].split(':')[-1].strip())
        self.f = float(x[2].split(':')[-1].strip())

    def show(self):
        return '{} ({}, {})'.format(self.f, self.p, self.r)

    def __lt__(self, other):
        return self.f < other.f


class M2ResultList(ResultList):
    def make_result(self, epoch):
        outdir = self.phasedir.make_outdir(epoch)
        return M2Result(outdir)

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

class M2ResultTable(ResultTable):
    def make_result_list(self, index):
        phasedir = SinglePhaseDir(index, self.dataset, self.phase)
        return M2ResultList(phasedir)

    def show(self):
        xs = [result_list.show() for result_list in self]

        max_list = self.maximum_list()
        ave_p = np.mean([x.p for x in max_list])
        ave_r = np.mean([x.r for x in max_list])
        ave_f = np.mean([x.f for x in max_list])
        line = 'average: {} ({}, {})'.format(ave_f, ave_p, ave_r)
        xs.append(line)

        return '\n'.join(xs)

