import numpy as np
from arteraro.auxt.expt.outdir import SinglePhaseDir
from .result import (
        Result,
        ResultList,
        ResultTable)

class GLEUResult(Result):
    def get_result_path(self):
        return self.outdir.make_path('result.txt')

    def init_attr(self, x):
        gleu = x[1].split(',')[0].replace("'", '').replace('[', '')
        self.gleu = float(gleu)

    def show(self):
        return '{}'.format(self.gleu)

    def __lt__(self, other):
        return self.gleu < other.gleu


class GLEUResultList(ResultList):
    def make_result(self, epoch):
        outdir = self.phasedir.make_outdir(epoch)
        return GLEUResult(outdir)

    def show(self):
        num_results = len(self)
        minimum = min(self)
        maximum = max(self)
        lst = ['index {} ({}):'.format(self.phasedir.index, num_results),
            'max {} ({}),'.format(maximum.gleu, maximum.outdir.epoch),
            'min {} ({})'.format(minimum.gleu, minimum.outdir.epoch)]
        line = '\t'.join(lst)
        return line


class GLEUResultTable(ResultTable):
    def make_result_list(self, index):
        phasedir = SinglePhaseDir(index, self.dataset, self.phase)
        return GLEUResultList(phasedir)

    def show(self):
        xs = [result_list.show() for result_list in self]

        max_list = self.maximum_list()
        ave = np.mean([x.gleu for x in max_list])
        line = 'average: {}'.format(ave)
        xs.append(line)

        return '\n'.join(xs)

