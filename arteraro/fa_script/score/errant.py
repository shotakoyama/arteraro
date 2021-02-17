from pathlib import Path
from arteraro.fa_script.score.run import ScoreRunScript

class ErrantScoreRunScript(ScoreRunScript):
    def append_source_path(self):
        path = Path(self.eval_config['errant_source_path']).resolve()
        self.append('   . {}'.format(path))

    def output_path(self):
        output = 'best.m2'
        result = 'result.res'
        result_cat1 = 'result.cat1'
        result_cat2 = 'result.cat2'
        result_cat3 = 'result.cat3'
        return output, result, result_cat1, result_cat2, result_cat3

    def make(self):
        original, reference, corrected = self.input_path()
        output, result, result_cat1, result_cat2, result_cat3 = self.output_path()
        self += [
            'errant_parallel -orig {} -cor {} -out {}'.format(original, corrected, output),
            'errant_compare -ref {} -hyp {} > {}'.format(reference, output, result),
            'errant_compare -ref {} -hyp {} -cat 1 > {}'.format(reference, output, result_cat1),
            'errant_compare -ref {} -hyp {} -cat 2 > {}'.format(reference, output, result_cat2),
            'errant_compare -ref {} -hyp {} -cat 3 > {}'.format(reference, output, result_cat3)]

