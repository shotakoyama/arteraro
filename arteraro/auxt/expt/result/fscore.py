import numpy as np
from .result import (
        Result,
        ResultList,
        ResultListFactory,
        ResultTable,
        ResultTableFactory)

class FScoreResult(Result):
    def show(self):
        return '{} ({}, {})'.format(self.f, self.p, self.r)

    def __lt__(self, other):
        return self.f < other.f


class FScoreResultList(ResultList):
    def show_avg(self):
        avg_p = np.mean([result.p for result in self])
        avg_r = np.mean([result.r for result in self])
        avg_f = np.mean([result.f for result in self])
        line = 'average: {} ({}, {})'.format(avg_f, avg_p, avg_r)
        return line

    def show_maxmin(self):
        num_results = len(self)
        minimum = min(self)
        maximum = max(self)
        max_result = 'max {} ({}), ({}, {}),'.format(
                maximum.f, maximum.outdir.epoch, maximum.p, maximum.r)
        min_result = 'min {} ({}), ({}, {})'.format(
                minimum.f, minimum.outdir.epoch, minimum.p, minimum.r)
        line = '{}\t{}'.format(max_result, min_result)
        return line


class FScoreResultListFactory(ResultListFactory):
    def init_result_list(self):
        return FScoreResultList()


class FScoreResultTable(ResultTable):
    def show(self):
        xs = ['index {} ({}): {}'.format(
            max(result_list).outdir.index,
            len(result_list),
            result_list.show_maxmin())
            for result_list in self]

        max_list = self.maximum_list()
        avg_p = np.mean([x.p for x in max_list])
        avg_r = np.mean([x.r for x in max_list])
        avg_f = np.mean([x.f for x in max_list])
        line = 'average: {} ({}, {})'.format(avg_f, avg_p, avg_r)
        xs.append(line)

        return '\n'.join(xs)


class FScoreResultTableFactory(ResultTableFactory):
    def init_result_table(self):
        return FScoreResultTable()

