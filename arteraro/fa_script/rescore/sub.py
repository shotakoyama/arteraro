from arteraro.fa_script.util.output import OutputSubScript
from arteraro.fa_script.util.base import make_ensemble_base_dir

class RescoreRegenerateSubScript(OutputSubScript):
    def __init__(self, dataset):
        super().__init__('rescore', dataset, 'rt_G.small', 1)

    def get_sub_script_name(self):
        return '{}_{}.sh'.format(self.phase, self.dataset)

    def make(self):
        self.append_command(make_ensemble_base_dir(self.dataset, 'valid'))
        self.append_command(make_ensemble_base_dir(self.dataset, 'test'))

class RescoreScoreSubScript(OutputSubScript):
    def __init__(self, dataset, stage):
        self.stage = stage
        super().__init__('rescore_score', dataset, 'rt_C.small', 1)

    def get_sub_script_name(self):
        return '{}_{}_{}.sh'.format(self.phase, self.dataset, self.stage)

    def make(self):
        for l in self.config['rescore']['lambda']:
            lmil = int(l * 1000)
            base_dir = make_ensemble_base_dir(self.dataset, self.stage)
            code_path = base_dir / 'score.{}.sh'.format(lmil)
            self.append_command(base_dir, code_path = code_path)

