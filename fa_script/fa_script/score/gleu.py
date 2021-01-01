from fa_script.score.run import ScoreRunScript

class GleuScoreRunScript(ScoreRunScript):
    def output_path(self):
        result = 'result.res'
        return result

    def make(self):
        scorer_path = self.eval_config['jfleg']['gleu_scorer']
        reference, source, corrected = self.input_path()
        result = self.output_path()
        self.append('python {} -r {} -s {} --hyp {} > {}'.format(scorer_path, reference, source, corrected, result))

