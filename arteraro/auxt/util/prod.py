from itertools import product
from .load import load_config
from .num_iter import get_num_train_iter

def make_train_indices():
    return [x for x in range(get_num_train_iter())]

def make_epoch_indices():
    config = load_config()
    start = config['generate']['epoch'].get('start', 1)
    end = config['generate']['epoch'].get('end', config['train']['max_epoch'])
    step = config['generate']['epoch'].get('step', 1)
    return range(start, end + 1, step)

def make_width_indices():
    config = load_config()
    return config['generate']['beam']

def make_expt_width_prod():
    return product(make_expt_indices(), make_width_indices())

def make_lambda_indices():
    config = load_config()
    return config['rescore']['lambda']

