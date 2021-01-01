from itertools import product

def make_index_list(config):
    return range(len(config['seed_list']))

def make_epoch_list(config):
    start = config['generate']['epoch'].get('start', 1)
    step = config['generate']['epoch'].get('step', 1)
    max_epoch = config['train']['max_epoch']
    epochs = range(start, max_epoch + 1, step)
    return epochs

def make_prod(config):
    return product(make_index_list(config), make_epoch_list(config))

