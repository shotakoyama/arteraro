from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config, load_eval_config
from fa_script.util.script import RunScript, SubScript
from fa_script.util.generate import make_prod, make_base_dir
from fa_script.util.output import ScoreSubScript

class Bea19ScoreRunScript(RunScript):
    def __init__(self, config, eval_config, base_dir, original, corrected, reference):
        self.eval_config = eval_config
        self.base_dir = base_dir
        self.original = original
        self.corrected = corrected
        self.reference = reference
        super().__init__(config)

    def append_source_path(self):
        path = Path(self.eval_config['bea19']['source_path']).resolve()
        self.append('   . {}'.format(path))

    def make(self):
        output = self.base_dir / 'bea19_valid.m2'
        result = self.base_dir / 'bea19_valid.res'
        result_cat1 = self.base_dir / 'bea19_valid.cat1'
        result_cat2 = self.base_dir / 'bea19_valid.cat2'
        result_cat3 = self.base_dir / 'bea19_valid.cat3'
        self += [
            'errant_parallel -orig {} -cor {} -out {}'.format(self.original, self.corrected, output),
            'errant_compare -ref {} -hyp {} > {}'.format(self.reference, output, result),
            'errant_compare -ref {} -hyp {} -cat 1 > {}'.format(self.reference, output, result_cat1),
            'errant_compare -ref {} -hyp {} -cat 2 > {}'.format(self.reference, output, result_cat2),
            'errant_compare -ref {} -hyp {} -cat 3 > {}'.format(self.reference, output, result_cat3)]

def main():
    config = load_config()
    eval_config = load_eval_config(config)
    prod = make_prod(config)

    for index, epoch, beam, lenpen in prod:
        base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
        script_path = base_dir / 'score_bea19.sh'
        original = eval_config['bea19']['valid_orig']
        corrected = base_dir / 'bea19_valid.txt'
        reference = eval_config['bea19']['valid_m2']
        script = Bea19ScoreRunScript(config, eval_config, base_dir, original, corrected, reference)
        with open(script_path, 'w') as f:
            print(script, file=f)

    if check_sub_config():
        sub_config = load_sub_config()
        sub_script = ScoreSubScript('bea19', config, sub_config, eval_config)
        with open('score_bea19.sh', 'w') as f:
            print(sub_script, file=f)

