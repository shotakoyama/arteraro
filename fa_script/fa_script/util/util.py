from pathlib import Path
import yaml

def load_config(path = None):
    if path is None:
        path = 'config.yaml'
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

def check_sub_config(path = None):
    if path is None:
        path = 'sub_config.yaml'
    return Path(path).exists()

def load_sub_config(path = None):
    if path is None:
        path = 'sub_config.yaml'
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

