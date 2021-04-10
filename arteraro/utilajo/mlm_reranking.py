import sys
import yaml
from argparse import ArgumentParser

def rerank_sentence(l, sent):
    score = sent['score'] + l * sent['mlm_score']
    sent['score'] = score
    return sent

def reranking(l, f):
    yml = yaml.safe_load(f)
    yml = [[rerank_sentence(l, sent) for sent in lst] for lst in yml]
    yml = yaml.safe_dump(yml)
    print(yml)

def main():
    parser = ArgumentParser()
    parser.add_argument('-l', type=float)
    args = parser.parse_args()

    reranking(args.l, sys.stdin)

