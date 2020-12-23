from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_config_and_sub_config
from fa_script.util.train import TrainRunScript, TrainSubScript

def run():
    config = load_config()
    seed_list = config['seed_list']
    for n in range(len(seed_list)):
        base_dir = Path(str(n)).resolve()
        base_dir.mkdir(exist_ok=True)
        script = TrainRunScript(config, n, base_dir)
        with open(base_dir / 'pretrain.sh', 'w') as f:
            f.write(str(script))

def sub():
    config, sub_config = load_config_and_sub_config()
    sub_script = TrainSubScript(config, sub_config, 'pretrain')
    with open('pretrain.sh', 'w') as f:
        f.write(str(sub_script))

def main():
    run()
    if check_sub_config():
        sub()

