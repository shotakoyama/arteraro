from pathlib import Path
from arteraro.fa_script.util.load import load_config, check_sub_config
from arteraro.fa_script.util.prod import make_index_list
from arteraro.fa_script.util.train import TrainRunScript, TrainSubScript

def run():
    for n in make_index_list(load_config()):
        base_dir = Path(str(n)).resolve()
        base_dir.mkdir(exist_ok=True)
        script = TrainRunScript(n, base_dir)
        with open(base_dir / 'finetune.sh', 'w') as f:
            f.write(str(script))

def sub():
    sub_script = TrainSubScript('finetune')
    with open('finetune.sh', 'w') as f:
        f.write(str(sub_script))

def main():
    run()
    if check_sub_config():
        sub()

