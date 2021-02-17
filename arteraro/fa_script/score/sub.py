from arteraro.fa_script.util.output import SingleOutputSubScript, EnsembleOutputSubScript
from arteraro.fa_script.util.prod import make_prod
from arteraro.fa_script.util.base import make_base_dir, make_ensemble_base_dir

class SingleScoreSubScript(SingleOutputSubScript):
    def __init__(self, dataset, stage):
        super().__init__('score', dataset, stage, 'rt_C.small', 1)

class ValidSingleScoreSubScript(SingleScoreSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'valid')

    def make(self):
        for index, epoch in make_prod(self.config):
            self.append_command(make_base_dir(index, self.dataset, self.stage, epoch))

class TestSingleScoreSubScript(SingleScoreSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'test')

    def make(self):
        for result in self.make_result_table().maximum_list():
            self.append_command(make_base_dir(result.index, self.dataset, self.stage, result.epoch))

class EnsembleScoreSubScript(EnsembleOutputSubScript):
    def __init__(self, dataset, stage):
        super().__init__('score', dataset, stage, 'rt_C.small', 1)

class ValidEnsembleScoreSubScript(EnsembleScoreSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'valid')

    def make(self):
        self.append_command(make_ensemble_base_dir(self.dataset, 'valid'))

class TestEnsembleScoreSubScript(EnsembleScoreSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'test')

    def make(self):
        self.append_command(make_ensemble_base_dir(self.dataset, 'test'))

