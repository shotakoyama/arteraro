from fa_script.util.prod import make_index_list, make_epoch_list
from fa_script.util.base import make_base_dir, make_ensemble_base_dir
from fa_script.util.load import load_config

class Result:
    def __init__(self, index, epoch, result_path, l=0.0):
        self.index = index
        self.epoch = epoch
        self.l = l
        self.init_attr(self.read_result(result_path))

    def read_result(self, result_path):
        with open(result_path) as f:
            x = f.readlines()
        return x

    def __lt__(self, other):
        return self.f < other.f

class ResultList(list):
    def __init__(self, dataset, stage, index):
        self.config = load_config()
        self.dataset = dataset
        self.stage = stage
        self.index = index
        self.make()

    def add(self, epoch, output):
        try:
            result = self.make_result(epoch, output)
            self.append(result)
        except IndexError:
            pass

    def make(self):
        for epoch in make_epoch_list(self.config):
            base_dir = make_base_dir(self.index, self.dataset, self.stage, epoch)
            self.add(epoch, base_dir / 'result.res')

class ResultTable(list):
    def __init__(self, dataset, stage):
        self.config = load_config()
        self.dataset = dataset
        self.stage = stage
        self.make()

    def make(self):
        for index in make_index_list(self.config):
            self.append(self.make_result_list(index))

    def maximum_list(self):
        return [max(result_list) for result_list in self]

def make_ensemble_result(result_class, dataset, stage):
    base_dir = make_ensemble_base_dir(dataset, stage)
    result_path = base_dir / 'result.res'
    if result_path.exists():
        result = result_class(None, None, result_path)
    else:
        result = None
    return result

def make_rescore_result_list(result_class, dataset, stage):
    config = load_config()
    result_list = []
    for l in config['rescore']['lambda']:
        base_dir = make_ensemble_base_dir(dataset, stage)
        lmil = int(l * 1000)
        output = base_dir / 'result.{}.res'.format(lmil)
        if output.exists():
            result = result_class(None, None, output, l = l)
            result_list.append(result)
    return result_list

