from arteraro.auxt.util.load import load_config

def get_arch_list():
    config = load_config()
    if 'arch_list' in config['rerank']:
        arch_list = config['rerank']['arch_list']
    else:
        arch_list = ['roberta_large']
    return arch_list

def get_lambda_list():
    config = load_config()
    return config['rerank']['lambda']

