from arteraro.fa_script.score.run import ScoreRunScript

class M2ScoreRunScript(ScoreRunScript):
    def output_path(self):
        result = 'result.res'
        return result

    def make(self):
        scorer_path = self.eval_config['conll']['m2_scorer']
        corrected, reference = self.input_path()
        result = self.output_path()
        self.append('{} {} {} > {}'.format(scorer_path, corrected, reference, result))

