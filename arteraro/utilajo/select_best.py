import sys
import yaml

def main():
    yml = yaml.safe_load(sys.stdin)
    for lst in yml:
        lst.sort(key=lambda x : x['score'])
        print(lst[-1]['text'])

