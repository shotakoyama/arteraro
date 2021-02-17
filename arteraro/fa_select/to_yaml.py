import sys
from argparse import ArgumentParser
import yaml
from arteraro.reguligilo.util import load_reverse

space = chr(0x2581)
rule = load_reverse()

def remove_bpe(x):
    x = x.strip()
    x = x.split()
    x = ''.join(x)
    x = x.replace(space, ' ')
    x = x.strip()
    return x

class Sentence:
    def __init__(self, x, retain_whitespace, retain_normalized):
        x = x.split('\t')
        self.index = int(x[0].split('-')[1])
        self.score = float(x[1])
        self.sent = x[2]

        if not retain_whitespace:
            self.sent = remove_bpe(self.sent)

        if not retain_normalized:
            for src, trg in rule:
                self.sent = self.sent.replace(src, trg)

    def __lt__(self, other):
        return self.score < other.score

    def as_dict(self):
        return {'score': self.score, 'text': self.sent}

def main():
    parser = ArgumentParser()
    parser.add_argument('--retain-whitespace', action = 'store_true')
    parser.add_argument('--retain-normalized', action = 'store_true')
    args = parser.parse_args()

    sent_list = []
    for x in sys.stdin:
        if x.startswith('H-'):
            sent_list.append(Sentence(x, args.retain_whitespace, args.retain_normalized))

    indices = [sent.index for sent in sent_list]
    num_sents = max(indices) + 1
    lst = [[] for _ in range(num_sents)]
    for sent in sent_list:
        lst[sent.index].append(sent.as_dict())

    print(yaml.safe_dump(lst))

