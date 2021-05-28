import numpy as np
from .result import (
        Result,
        ResultList,
        ResultListFactory,
        ResultTable,
        ResultTableFactory)

class GLEUResult(Result):
    def init_attr(self, x):
        gleu = x[1].split(',')[0].replace("'", '').replace('[', '')
        self.gleu = float(gleu)

    def show(self):
        return '{}'.format(self.gleu)

    def __lt__(self, other):
        return self.gleu < other.gleu


class GLEUResultList(ResultList):
    def show_avg(self):
        avg = np.mean([result.gleu for result in self])
        line = 'average: {}'.format(avg)
        return line

    def show_maxmin(self):
        num_results = len(self)
        minimum = min(self)
        maximum = max(self)
        max_result = 'max {} ({})'.format(
                maximum.gleu, maximum.outdir.epoch)
        min_result = 'min {} ({})'.format(
                minimum.gleu, minimum.outdir.epoch)
        line = '{}\t{}'.format(max_result, min_result)
        return line

    def show_best(self):
        num_results = len(self)
        maximum = max(self)
        max_result = 'max {}'.format(maximum.gleu)
        return max_result


class GLEUResultListFactory(ResultListFactory):
    def init_result_list(self):
        return GLEUResultList()

    def make_result(self, outdir):
        return GLEUResult(outdir)


class GLEUResultTable(ResultTable):
    def show(self):
        xs = ['index {} ({}): {}'.format(
            max(result_list).outdir.index,
            len(result_list),
            result_list.show_maxmin())
            for result_list in self]

        max_list = self.maximum_list()
        ave = np.mean([x.gleu for x in max_list])
        line = 'average: {}'.format(ave)
        xs.append(line)

        return '\n'.join(xs)


class GLEUResultTableFactory(ResultTableFactory):
    def init_result_table(self):
        return GLEUResultTable()

    def make_result_list_factory(self):
        return GLEUResultListFactory()

