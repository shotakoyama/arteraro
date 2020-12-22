from pathlib import Path
from itertools import product
from fa_script.util.qsub import qsub_command
from fa_script.util.script import RunScript
from fa_script.util.fairseq import fairseq_interactive_command

def make_prod_helper(config):
    indices = range(len(config['seed_list']))
    start = config['generate']['epoch'].get('start', 1)
    step = config['generate']['epoch'].get('step', 1)
    max_epoch = config['train']['max_epoch']
    epochs = range(start, max_epoch + 1, step)
    beams = config['generate'].get('beam', [12])
    lenpens = config['generate'].get('lenpen', [0.6])
    return indices, epochs, beams, lenpens

def make_prod_without_index_and_epoch(config):
    _, _, beams, lenpens = make_prod_helper(config)
    prod = product(beams, lenpens)
    return prod

def make_prod_without_index(config):
    _, epochs, beams, lenpens = make_prod_helper(config)
    prod = product(epochs, beams, lenpens)
    return prod

def make_prod(config):
    indices, epochs, beams, lenpens = make_prod_helper(config)
    prod = product(indices, epochs, beams, lenpens)
    return prod

def make_base_dir(index, dataset, epoch, beam, lenpen):
    return Path(str(index)).resolve() / dataset / str(epoch) / str(beam) / str(int(lenpen * 100))

def make_ensemble_base_dir(dataset, beam, lenpen):
    return Path('ensemble').resolve() / dataset / str(beam) / str(int(lenpen * 100))

class GenerateRunScript(RunScript):
    def __init__(self, config, base_dir, checkpoint, beam, batch_size, lenpen, source, output, select):
        self.checkpoint = checkpoint
        self.beam = beam
        self.batch_size = batch_size
        self.lenpen = lenpen
        self.source = source
        self.output = output
        self.select = select
        super().__init__(config, base_dir)

    def make(self):
        data_bin = self.get_data_bin()
        command = fairseq_interactive_command(
                data_bin, self.checkpoint, self.beam, self.buffer_size,
                self.batch_size, self.lenpen, self.source, self.output)
        self.append(command)
        self.append('cat {} | select_best > {}'.format(self.output, self.select))

