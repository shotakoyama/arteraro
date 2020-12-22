from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config, load_eval_config
from fa_script.util.script import RunScript
from fa_script.util.generate import make_prod, make_prod_without_index_and_epoch, make_base_dir, make_ensemble_base_dir
from fa_script.util.output import SingleScoreSubScript, EnsembleScoreSubScript

class Bea19ScoreRunScript(RunScript):
    def __init__(self, config, eval_config, base_dir, corrected):
        self.eval_config = eval_config
        self.corrected = corrected
        super().__init__(config, base_dir)

    def append_source_path(self):
        path = Path(self.eval_config['bea19']['source_path']).resolve()
        self.append('   . {}'.format(path))

    def output_path(self):
        output = 'bea19_valid.m2'
        result = 'bea19_valid.res'
        result_cat1 = 'bea19_valid.cat1'
        result_cat2 = 'bea19_valid.cat2'
        result_cat3 = 'bea19_valid.cat3'
        return output, result, result_cat1, result_cat2, result_cat3

    def make(self):
        original = self.eval_config['bea19']['valid_orig']
        reference = self.eval_config['bea19']['valid_m2']
        output, result, result_cat1, result_cat2, result_cat3 = self.output_path()
        self += [
            'errant_parallel -orig {} -cor {} -out {}'.format(original, self.corrected, output),
            'errant_compare -ref {} -hyp {} > {}'.format(reference, output, result),
            'errant_compare -ref {} -hyp {} -cat 1 > {}'.format(reference, output, result_cat1),
            'errant_compare -ref {} -hyp {} -cat 2 > {}'.format(reference, output, result_cat2),
            'errant_compare -ref {} -hyp {} -cat 3 > {}'.format(reference, output, result_cat3)]

def write_run_script(config, eval_config, base_dir):
    corrected = 'bea19_valid.txt'
    script = Bea19ScoreRunScript(config, eval_config, base_dir, corrected)
    script_path = base_dir / 'score_bea19.sh'
    with open(script_path, 'w') as f:
        f.write(str(script))

def single_run():
    config, eval_config = load_config_and_eval_config()
    prod = make_prod(config)
    for index, epoch, beam, lenpen in prod:
        base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
        write_run_script(config, eval_config, base_dir)

def ensemble_run():
    config, eval_config = load_config_and_eval_config()
    prod = make_prod_without_index_and_epoch(config)
    for beam, lenpen in prod:
        base_dir = make_ensemble_base_dir('bea19', beam, lenpen)
        write_run_script(config, eval_config, base_dir)

def single_sub():
    config, sub_config, eval_config = load_config_and_sub_config_and_eval_config()
    sub_script = SingleScoreSubScript('bea19', config, sub_config, eval_config)
    with open('score_bea19.sh', 'w') as f:
        f.write(str(sub_script))

def ensemble_sub():
    config, sub_config, eval_config = load_config_and_sub_config_and_eval_config()
    sub_script = EnsembleScoreSubScript('bea19', config, sub_config, eval_config)
    with open('ens_score_bea19.sh', 'w') as f:
        f.write(str(sub_script))

def single():
    single_run()
    if check_sub_config():
        single_sub()

def ensemble():
    ensemble_run()
    if check_sub_config():
        ensemble_sub()

