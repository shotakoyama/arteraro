from pathlib import Path
import yaml

class ConfigContainer:
    def __init__(self):
        self.config = None

    def __call__(self):
        if self.config is None:
            with open('auxt.yaml') as f:
                self.config = yaml.safe_load(f)
        return self.config

class SubConfigContainer:
    def __init__(self):
        self.sub_config = None

    def __call__(self):
        if self.sub_config is None:
            with open('sub.yaml') as f:
                self.sub_config = yaml.safe_load(f)
        return self.sub_config

class EvalConfigContainer:
    def __init__(self, config_container):
        self.config_container = config_container
        self.eval_config = None

    def __call__(self):
        if self.eval_config is None:
            with open(self.config_container()['eval_config']) as f:
                self.eval_config = yaml.safe_load(f)
        return self.eval_config

def check_sub_config():
    return Path('sub.yaml').exists()

load_config = ConfigContainer()
load_sub_config = SubConfigContainer()
load_eval_config = EvalConfigContainer(load_config)

def load_config_and_eval_config():
    return load_config(), load_eval_config()

def load_config_and_sub_config():
    return load_config(), load_sub_config()

def load_config_and_sub_config_and_eval_config():
    return load_config(), load_sub_config(), load_eval_config()

