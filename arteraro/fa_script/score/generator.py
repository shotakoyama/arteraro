from arteraro.fa_script.util.prod import make_index_list, make_prod
from arteraro.fa_script.util.base import make_base_dir, make_ensemble_base_dir
from arteraro.fa_script.util.load import load_config_and_eval_config

class ScoreRunScriptGenerator:
    def __init__(self, dataset, script_class):
        self.dataset = dataset
        self.script_class = script_class
        self.config, self.eval_config = load_config_and_eval_config()

    def write(self, base_dir):
        script = self.script_class(base_dir)
        with open(base_dir / script.get_script_name(), 'w') as f:
            f.write(str(script))

class ValidSingleScoreRunScriptGenerator(ScoreRunScriptGenerator):
    def __call__(self):
        for index, epoch in make_prod(self.config):
            self.write(make_base_dir(index, self.dataset, 'valid', epoch))

class TestSingleScoreRunScriptGenerator(ScoreRunScriptGenerator):
    def __call__(self):
        for result in self.make_result_table().maximum_list():
            self.write(make_base_dir(result.index, self.dataset, 'test', result.epoch))

class ValidEnsembleScoreRunScriptGenerator(ScoreRunScriptGenerator):
    def __call__(self):
        self.write(make_ensemble_base_dir(self.dataset, 'valid'))

class TestEnsembleScoreRunScriptGenerator(ScoreRunScriptGenerator):
    def __call__(self):
        self.write(make_ensemble_base_dir(self.dataset, 'test'))

