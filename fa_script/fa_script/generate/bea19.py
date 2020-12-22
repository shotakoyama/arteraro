from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config, load_eval_config
from fa_script.util.generate import make_prod, make_prod_without_index_and_epoch, make_base_dir, make_ensemble_base_dir, GenerateRunScript
from fa_script.util.output import SingleGenerateSubScript, EnsembleGenerateSubScript
from fa_script.result.bea19 import make_bea19_result_table

class Bea19GenerateRunScript(GenerateRunScript):
    buffer_size = 4384

    def get_data_bin(self):
        return Path(self.config['data']).resolve() / '0' / 'data-bin'

def ensemble_checkpoint_path(config):
    result_table = make_bea19_result_table(config)
    maximum_list = [max(result_list) for result_list in result_table]
    path_list = [Path(str(result.index)).resolve() / 'checkpoints' / 'checkpoint{}.pt'.format(result.epoch) for result in maximum_list]
    path_list = [str(x) for x in path_list]
    checkpoint_path = ':'.join(path_list)
    return checkpoint_path

def write_run_script(config, base_dir, checkpoint_path, beam, batch_size, lenpen, source):
    script_path = base_dir / 'gen_bea19.sh'
    output = 'bea19_valid.yaml'
    select = 'bea19_valid.txt'
    script = Bea19GenerateRunScript(config, base_dir, checkpoint_path, beam, batch_size, lenpen, source, output, select)
    with open(script_path, 'w') as f:
        f.write(str(script))

def single_run():
    config = load_config()
    eval_config = load_eval_config(config)
    prod = make_prod(config)
    batch_size = config['generate']['batch_size']
    source = eval_config['bea19']['valid_src']
    for index, epoch, beam, lenpen in prod:
        base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
        base_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_path = Path(str(index)).resolve() / 'checkpoints' / 'checkpoint{}.pt'.format(epoch)
        write_run_script(config, base_dir, checkpoint_path, beam, batch_size, lenpen, source)

def ensemble_run():
    config = load_config()
    eval_config = load_eval_config(config)
    prod = make_prod_without_index_and_epoch(config)
    checkpoint_path = ensemble_checkpoint_path(config)
    batch_size = config['generate']['ensemble_batch_size']
    source = eval_config['bea19']['valid_src']
    for beam, lenpen in prod:
        base_dir = make_ensemble_base_dir('bea19', beam, lenpen)
        base_dir.mkdir(parents=True, exist_ok=True)
        write_run_script(config, base_dir, checkpoint_path, beam, batch_size, lenpen, source)

def single_sub():
    config = load_config()
    sub_config = load_sub_config()
    eval_config = load_eval_config(config)
    sub_script = SingleGenerateSubScript('bea19', config, sub_config, eval_config)
    with open('gen_bea19.sh', 'w') as f:
        f.write(str(sub_script))

def ensemble_sub():
    config = load_config()
    sub_config = load_sub_config()
    eval_config = load_eval_config(config)
    sub_script = EnsembleGenerateSubScript('bea19', config, sub_config, eval_config)
    with open('ens_gen_bea19.sh', 'w') as f:
        print(sub_script, file=f)

def single():
    single_run()
    if check_sub_config():
        single_sub()

def ensemble():
    ensemble_run()
    if check_sub_config():
        ensemble_sub()

