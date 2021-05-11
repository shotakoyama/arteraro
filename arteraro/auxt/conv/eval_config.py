import sys
import yaml
from pathlib import Path

def convert_path_absolute(dct):
    for key, value in dct.items():
        if type(value) == str:
            dct[key] = str(Path(value).resolve())
        elif type(value) == list:
            dct[key] = [str(Path(x).resolve()) for x in value]
        elif type(value) == dict:
            dct[key] = convert_path_absolute(value)
        else:
            assert False
    return dct

def convert_eval_config():
    config = yaml.safe_load(sys.stdin)
    config = convert_path_absolute(config)
    config = yaml.safe_dump(config)
    print(config)

