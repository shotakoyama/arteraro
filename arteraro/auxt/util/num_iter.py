from arteraro.auxt.util.load import load_config

def get_num_train_iter():
    config = load_config()
    if 'iter' in config:
        num_iter = config['num_iter']
    elif 'data_indices' in config:
        num_iter = len(config['data_indices'])
    elif 'seed_list' in config['train']:
        num_iter = len(config['train']['seed_list'])
    else:
        assert False
    return num_iter

