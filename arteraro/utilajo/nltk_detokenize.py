import sys
from nltk.tokenize.treebank import TreebankWordDetokenizer

def main():
    for x in sys.stdin:
        x = x.strip()
        x = TreebankWordDetokenizer().detokenize(x.split())
        print(x)

