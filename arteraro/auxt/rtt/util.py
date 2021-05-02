from arteraro.auxt.util.load import load_config

def get_num_indices():
    config = load_config()
    return [x for x in range(config['indices'])]

def get_num_segments():
    config = load_config()
    return [x for x in range(config['segments'])]

def get_bridge_language_list():
    config = load_config()
    return list(config['bridges'])

