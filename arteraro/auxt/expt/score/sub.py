from arteraro.auxt.expt.sub import ExptSubScript

class ScoreSubScript(ExptSubScript):
    def make_h_rt(self):
        return self.sub_config['score']['h_rt']

    def make_node(self):
        return self.sub_config['score'].get('node', 'rt_C.small')

    def make_num_node(self):
        return self.sub_config['score'].get('num_node', 1)

class ValidScoreSubScript(ScoreSubScript):
    def make_path(self):
        return 'score_valid.sh'

class TestScoreSubScript(ScoreSubScript):
    def make_path(self):
        return 'score_test.sh'

class EnsembleScoreSubScript(ScoreSubScript):
    def make_path(self):
        return 'score_ensemble.sh'

