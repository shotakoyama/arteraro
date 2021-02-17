import sys
import yaml
from argparse import ArgumentParser

def main():
    yml = yaml.safe_load(sys.stdin)
    for lst in yml:
        lst.sort(key=lambda x : x['score'])
        print(lst[-1]['text'])

def remake_dict(l, sent):
    return {
        'text': sent['text'],
        'org_score': sent['org_score'],
        'mlm_score': sent['mlm_score'],
        'score': sent['org_score'] + l * sent['mlm_score']}

def rescore():
    parser = ArgumentParser()
    parser.add_argument('-l', type=float)
    args = parser.parse_args()

    yml = yaml.safe_load(sys.stdin)
    yml = [[remake_dict(args.l, sent) for sent in lst]for lst in yml]
    print(yaml.safe_dump(yml))


