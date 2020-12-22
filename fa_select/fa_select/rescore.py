import sys
import yaml
import torch
from tqdm import tqdm
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from transformers import RobertaForMaskedLM, RobertaTokenizer
from sacremoses import MosesDetokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer

class RobertaMLM:
    def __init__(self, detokenize):
        self.tokenizer = RobertaTokenizer.from_pretrained('roberta-large')
        self.detokenize = detokenize
        if self.detokenize:
            self.md = MosesDetokenizer(lang='en')
        self.mask_id = self.tokenizer('<mask>')['input_ids'][1]
        self.model = RobertaForMaskedLM.from_pretrained('roberta-large')
        self.model.eval()
        self.model.to('cuda')

    def detokenizer(self, sent):
        sent = self.md.detokenize(sent.split(' '))
        sent = TreebankWordDetokenizer().detokenize(sent.split(' '))
        return sent

    def __call__(self, src_text):
        src = self.tokenizer(src_text)['input_ids']
        masked_src = torch.tensor(src).repeat(1, len(src) - 2).reshape(len(src) - 2, len(src))
        mask = torch.ones(len(src)).diag()[1:-1]
        masked_src.masked_fill_(mask > 0, self.mask_id)
        masked_src = masked_src.to('cuda')
        with torch.no_grad():
            out = self.model(masked_src)[0]
        pred = torch.stack([out[n - 1, n] for n in range(1, len(src) - 1)])
        pred = torch.log_softmax(pred, dim = -1).to('cpu')
        pred = [y[t] for t, y in zip(src[1:-1], pred)]
        score = sum(pred).item()
        penalty = (5 + len(src) - 2) / (5 + 1)
        return score / penalty

def rescore(mlm, sent):
    org_score = sent['score']
    text = sent['text']
    if mlm.detokenize:
        detokenized_text = mlm.detokenizer(text)
        mlm_score = mlm(detokenized_text)
        dct = {'text': text, 'org_score': org_score, 'mlm_score': mlm_score, 'detokenized_text': detokenized_text}
    else:
        mlm_score = mlm(text)
        dct = {'text': text, 'org_score': org_score, 'mlm_score': mlm_score}
    return dct

def main():
    parser = ArgumentParser()
    parser.add_argument('--detokenize', action = 'store_true')
    args = parser.parse_args()

    lst = yaml.safe_load(sys.stdin)
    mlm = RobertaMLM(args.detokenize)
    lst = [[rescore(mlm, sent) for sent in beam] for beam in tqdm(lst)]
    yml = yaml.safe_dump(lst)
    print(yml)

