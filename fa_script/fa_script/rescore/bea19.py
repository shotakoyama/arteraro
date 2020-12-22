from pathlib import Path
from fa_script.util.util import check_sub_config, load_config_and_eval_config, load_config_and_sub_config_and_eval_config
from fa_script.util.script import RunScript
from fa_script.util.generate import make_prod_without_index_and_epoch, make_ensemble_base_dir
from fa_script.util.output import RescoreSubScript, OutputSubScript
from fa_script.score.bea19 import Bea19ScoreRunScript

class Bea19RescoreRunScript(RunScript):
    def make(self):
        source_yaml = 'bea19_valid.yaml'
        target_yaml = 'bea19_valid_rescored.yaml'
        self.append('roberta_rescore --detokenize < {} > {}'.format(source_yaml, target_yaml))
        for l in self.config['rescore']['lambda']:
            lmil = int(l * 1000)
            target_text = 'bea19_valid_rescored.{}.txt'.format(lmil)
            self.append('select_with_lambda -l {} < {} > {} &'.format(l, target_yaml, target_text))
        self.append('wait')

class Bea19RescoreScoreRunScript(Bea19ScoreRunScript):
    def __init__(self, config, eval_config, base_dir, l, corrected):
        self.l = l
        super().__init__(config, eval_config, base_dir, corrected)

    def output_path(self):
        lmil = int(self.l * 1000)
        output = 'bea19_valid.{}.m2'.format(lmil)
        result = 'bea19_valid.{}.res'.format(lmil)
        result_cat1 = 'bea19_valid.{}.cat1'.format(lmil)
        result_cat2 = 'bea19_valid.{}.cat2'.format(lmil)
        result_cat3 = 'bea19_valid.{}.cat3'.format(lmil)
        return output, result, result_cat1, result_cat2, result_cat3

class RescoreScoreSubScript(OutputSubScript):
    def __init__(self, config, sub_config, eval_config):
        self.phase = 'rescore_score'
        self.phase_abbrev = 'rescore_score'
        self.default_node = 'rt_C.small'
        self.default_num_node = 1
        super().__init__('bea19', config, sub_config, eval_config)

    def make(self):
        prod = make_prod_without_index_and_epoch(self.config)
        for beam, lenpen in prod:
            for l in self.config['rescore']['lambda']:
                base_dir = make_ensemble_base_dir(self.dataset, beam, lenpen)
                lmil = int(l * 1000)
                code_path = base_dir / 'rescore_score_bea19.{}.sh'.format(lmil)
                self.append_command(base_dir, code_path = code_path)

def run_rescore():
    config, eval_config = load_config_and_eval_config()
    prod = make_prod_without_index_and_epoch(config)
    for beam, lenpen in prod:
        base_dir = make_ensemble_base_dir('bea19', beam, lenpen)
        script = Bea19RescoreRunScript(config, base_dir)
        script_path = base_dir / 'rescore_bea19.sh'
        with open(script_path, 'w') as f:
            f.write(str(script))

def run_rescore_score():
    config, eval_config = load_config_and_eval_config()
    prod = make_prod_without_index_and_epoch(config)
    for beam, lenpen in prod:
        for l in config['rescore']['lambda']:
            base_dir = make_ensemble_base_dir('bea19', beam, lenpen)
            lmil = int(l * 1000)
            corrected = 'bea19_valid_rescored.{}.txt'.format(lmil)
            script = Bea19RescoreScoreRunScript(config, eval_config, base_dir, l, corrected)
            script_path = base_dir / 'rescore_score_bea19.{}.sh'.format(lmil)
            with open(script_path, 'w') as f:
                f.write(str(script))

def sub_rescore():
    config, sub_config, eval_config = load_config_and_sub_config_and_eval_config()
    sub_script = RescoreSubScript('bea19', config, sub_config, eval_config)
    with open('rescore_bea19.sh', 'w') as f:
        print(sub_script, file=f)

def sub_rescore_score():
    config, sub_config, eval_config = load_config_and_sub_config_and_eval_config()
    sub_script = RescoreScoreSubScript(config, sub_config, eval_config)
    with open('rescore_score_bea19.sh', 'w') as f:
        print(sub_script, file=f)

def main():
    run_rescore()
    run_rescore_score()
    if check_sub_config():
        sub_rescore()
        sub_rescore_score()

