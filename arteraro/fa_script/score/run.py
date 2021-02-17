from arteraro.fa_script.util.load import load_eval_config
from arteraro.fa_script.util.script import RunScript

class ScoreRunScript(RunScript):
    def __init__(self, base_dir):
        self.eval_config = load_eval_config()
        super().__init__(base_dir)

    def get_script_name(self):
        return 'score.sh'

