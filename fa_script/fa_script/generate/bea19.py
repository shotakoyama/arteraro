from pathlib import Path
from itertools import product
from fa_script.util.util import load_config, check_sub_config, load_sub_config, load_eval_config
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript, SubScript
from fa_script.util.fairseq import fairseq_interactive_command

def make_prod(config, eval_config):
    indices = range(len(config['seed_list']))
    start = config['generate']['epoch'].get('start', 1)
    step = config['generate']['epoch'].get('step', 1)
    max_epoch = config['train']['max_epoch']
    epochs = range(start, max_epoch + 1, step)
    beams = config['generate'].get('beam', [12])
    lenpens = config['generate'].get('lenpen', [0.6])
    prod = product(indices, epochs, beams, lenpens)
    return prod

class Bea19GenerateRunScript(RunScript):
    def __init__(self, config, checkpoint, beam, batch_size, lenpen, source, output):
        self.checkpoint = checkpoint
        self.beam = beam
        self.batch_size = batch_size
        self.lenpen = lenpen
        self.source = source
        self.output = output
        super().__init__(config)

    def make(self):
        data_bin = Path(self.config['data']).resolve() / '0' / 'data-bin'
        command = fairseq_interactive_command(data_bin, self.checkpoint, self.beam, 4384,
                self.batch_size, self.lenpen, self.source, self.output)
        self.append(command)

class Bea19GenerateSubScript(SubScript):
    def __init__(self, config, sub_config, eval_config):
        self.eval_config = eval_config
        super().__init__(config, sub_config)

    def make(self):
        prod = make_prod(self.config, self.eval_config)
        for index, epoch, beam, lenpen in prod:
            base_dir = Path(str(index)).resolve() / 'bea19' / str(epoch) / str(beam) / str(int(lenpen * 100))
            code_path = base_dir / 'gen_bea19.sh'
            group = self.sub_config['group']
            h_rt = self.sub_config['generate']['h_rt']
            node = self.sub_config['generate'].get('node', 'rt_G.small')
            num_node = self.sub_config['generate'].get('num_node', 1)
            workdir = str(base_dir)
            var_dict = {'WORKDIR': workdir, 'SGE_QSUB': 'yes'}
            command = qsub_command(code_path, group, h_rt, node, num_node, var_dict=var_dict)
            self.append(command)

def main():
    config = load_config()
    eval_config = load_eval_config(config)
    prod = make_prod(config, eval_config)

    batch_size = config['generate']['batch_size']
    source = eval_config['bea19']['valid_src']
    for index, epoch, beam, lenpen in prod:
        base_dir = Path(str(index)).resolve() / 'bea19' / str(epoch) / str(beam) / str(int(lenpen * 100))
        base_dir.mkdir(parents=True, exist_ok=True)
        script_path = base_dir / 'gen_bea19.sh'
        checkpoint_path = Path(str(index)).resolve() / 'checkpoints' / 'checkpoint{}.pt'.format(epoch)
        output = base_dir / 'bea19_valid.txt'
        script = Bea19GenerateRunScript(config, checkpoint_path, beam, batch_size, lenpen, source, output)
        with open(script_path, 'w') as f:
            print(script, file=f)

    if check_sub_config():
        sub_config = load_sub_config()
        sub_script = Bea19GenerateSubScript(config, sub_config, eval_config)
        with open('gen_bea19.sh', 'w') as f:
            print(sub_script, file=f)

