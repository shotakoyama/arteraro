import yaml
from pathlib import Path
from argparse import ArgumentParser

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

def main():
    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target')
    args = parser.parse_args()

    with open(args.source) as f:
        config = yaml.safe_load(f)
    with open(args.target, 'w') as f:
        config = convert_path_absolute(config)
        print(yaml.safe_dump(config), file = f)
