from pathlib import Path
from fa_script.util.util import load_config, check_sub_config, load_sub_config, load_eval_config
from fa_script.util.script import RunScript
from fa_script.util.fairseq import fairseq_interactive_command
from fa_script.util.generate import make_prod, make_base_dir
from fa_script.util.output import GenerateSubScript

class Bea19GenerateRunScript(RunScript):
    def __init__(self, config, checkpoint, beam, batch_size, lenpen, source, output, select):
        self.checkpoint = checkpoint
        self.beam = beam
        self.batch_size = batch_size
        self.lenpen = lenpen
        self.source = source
        self.output = output
        self.select = select
        super().__init__(config)

    def make(self):
        data_bin = Path(self.config['data']).resolve() / '0' / 'data-bin'
        command = fairseq_interactive_command(data_bin, self.checkpoint, self.beam, 4384,
                self.batch_size, self.lenpen, self.source, self.output)
        self.append(command)
        self.append('cat {} | select_best > {}'.format(self.output, self.select))

def main():
    config = load_config()
    eval_config = load_eval_config(config)
    prod = make_prod(config)

    batch_size = config['generate']['batch_size']
    source = eval_config['bea19']['valid_src']
    for index, epoch, beam, lenpen in prod:
        base_dir = make_base_dir(index, 'bea19', epoch, beam, lenpen)
        base_dir.mkdir(parents=True, exist_ok=True)
        script_path = base_dir / 'gen_bea19.sh'
        checkpoint_path = Path(str(index)).resolve() / 'checkpoints' / 'checkpoint{}.pt'.format(epoch)
        output = base_dir / 'bea19_valid.yaml'
        select = base_dir / 'bea19_valid.txt'
        script = Bea19GenerateRunScript(config, checkpoint_path, beam, batch_size, lenpen, source, output, select)
        with open(script_path, 'w') as f:
            print(script, file=f)

    if check_sub_config():
        sub_config = load_sub_config()
        sub_script = GenerateSubScript('bea19', config, sub_config, eval_config)
        with open('gen_bea19.sh', 'w') as f:
            print(sub_script, file=f)

