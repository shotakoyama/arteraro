from arteraro.auxt.util.prod import make_train_indices

class Result:
    def __init__(self, outdir):
        self.outdir = outdir
        self.init_attr(self.read_result())

    def read_result(self):
        result_path = self.get_result_path()
        with open(result_path) as f:
            x = f.readlines()
        return x


class ResultList(list):
    def __init__(self, phasedir):
        self.phasedir = phasedir
        self.make()

    def make(self):
        for epoch in self.phasedir.epoch_indices:
            try:
                result = self.make_result(epoch)
                self.append(result)
            except IndexError:
                pass


class ResultTable(list):
    def __init__(self, dataset, phase):
        self.dataset = dataset
        self.phase = phase
        self.make()

    def make(self):
        for index in make_train_indices():
            self.append(self.make_result_list(index))

    def maximum_list(self):
        return [max(result_list) for result_list in self]

    def maximum_indices(self):
        return [max(result_list).epoch for result_list in self]

