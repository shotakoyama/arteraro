from fa_script.util.output import SingleOutputSubScript, EnsembleValidTestOutputSubScript
from fa_script.util.prod import make_prod
from fa_script.util.base import make_base_dir, make_ensemble_base_dir

class SingleGenerateSubScript(SingleOutputSubScript):
    def __init__(self, dataset, stage):
        super().__init__('generate', dataset, stage, 'rt_G.small', 1)

class ValidSingleGenerateSubScript(SingleGenerateSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'valid')

    def make(self):
        for index, epoch in make_prod(self.config):
            self.append_command(make_base_dir(index, self.dataset, self.stage, epoch))

class TestSingleGenerateSubScript(SingleGenerateSubScript):
    def __init__(self, dataset):
        super().__init__(dataset, 'test')

    def make(self):
        for result in self.make_result_table().maximum_list():
            self.append_command(make_base_dir(result.index, self.dataset, self.stage, result.epoch))

class EnsembleGenerateSubScript(EnsembleValidTestOutputSubScript):
    def __init__(self, dataset):
        super().__init__('generate', dataset, 'rt_G.small', 1)

    def get_h_rt(self):
        return self.sub_config[self.phase].get('ensemble_h_rt', self.sub_config[self.phase]['h_rt'])

    def make(self):
        self.append_command(make_ensemble_base_dir(self.dataset, 'valid'))
        self.append_command(make_ensemble_base_dir(self.dataset, 'test'))

