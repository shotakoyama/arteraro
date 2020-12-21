from pathlib import Path
from itertools import product
from fa_script.util.qsub import qsub_command

def make_prod_helper(config):
    indices = range(len(config['seed_list']))
    start = config['generate']['epoch'].get('start', 1)
    step = config['generate']['epoch'].get('step', 1)
    max_epoch = config['train']['max_epoch']
    epochs = range(start, max_epoch + 1, step)
    beams = config['generate'].get('beam', [12])
    lenpens = config['generate'].get('lenpen', [0.6])
    return indices, epochs, beams, lenpens

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

