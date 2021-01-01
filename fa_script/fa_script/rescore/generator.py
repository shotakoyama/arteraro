from fa_script.util.output import OutputRunScriptGenerator
from fa_script.util.base import make_ensemble_base_dir

class RescoreRegenerateRunScriptGenerator(OutputRunScriptGenerator):
    def write(self, base_dir):
        script = self.script_class(base_dir)
        self.write_script(base_dir, script)

    def __call__(self):
        self.write(make_ensemble_base_dir(self.dataset, 'valid'))
        self.write(make_ensemble_base_dir(self.dataset, 'test'))

class RescoreScoreRunScriptGenerator(OutputRunScriptGenerator):
    def __init__(self, dataset, stage, script_class):
        self.stage = stage
        super().__init__(dataset, script_class)

    def write(self, base_dir, l):
        script = self.script_class(base_dir, l)
        self.write_script(base_dir, script)

    def __call__(self):
        for l in self.config['rescore']['lambda']:
            base_dir = make_ensemble_base_dir(self.dataset, self.stage)
            self.write(base_dir, l)

