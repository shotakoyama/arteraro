import sys
from argparse import ArgumentParser
import yaml
from arteraro.reguligilo.decoder import Decoder

space = chr(0x2581)
decoder = Decoder()


def remove_bpe(x):
    x = x.strip()
    x = x.split()
    x = ''.join(x)
    x = x.replace(space, ' ')
    x = x.strip()
    return x


class Sentence:
    retain_whitespace = False
    retain_normalized = False

    def __init__(self, x):
        x = x.split('\t')
        self.index = int(x[0].split('-')[1])
        self.score = float(x[1])
        self.sent = x[2]

        if not self.retain_whitespace:
            self.sent = remove_bpe(self.sent)

        if not self.retain_normalized:
            self.sent = decoder(self.sent)

    def __lt__(self, other):
        return self.score < other.score

    def as_dict(self):
        return {'score': self.score, 'text': self.sent}


def make_sentence_list(f):
    sent_list = []
    for x in f:
        if x.startswith('H-'):
            sent_list.append(Sentence(x))
    return sent_list


def make_beam_list(sent_list):
    indices = [sent.index for sent in sent_list]
    num_sents = max(indices) + 1
    lst = [[] for _ in range(num_sents)]
    for sent in sent_list:
        lst[sent.index].append(sent.as_dict())
    return lst


def main():
    parser = ArgumentParser()
    parser.add_argument('--retain-whitespace', action = 'store_true')
    parser.add_argument('--retain-normalized', action = 'store_true')
    args = parser.parse_args()

    Sentence.retain_whitespace = args.retain_whitespace
    Sentence.retain_normalized = args.retain_normalized

    sent_list = make_sentence_list(sys.stdin)
    beam_list = make_beam_list(sent_list)
    print(yaml.safe_dump(beam_list))

