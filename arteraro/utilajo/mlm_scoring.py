import sys
import yaml
import torch
from tqdm import tqdm
from argparse import ArgumentParser
from sacremoses import MosesDetokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from transformers import AutoTokenizer, AutoModelForMaskedLM

class MLMTokenizer:
    def __init__(self, name, detokenize):
        self.detokenize = detokenize
        if self.detokenize:
            self.md = MosesDetokenizer(lang='en')
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.pad_id = self.tokenizer.encoder['<pad>']
        self.mask_id = self.tokenizer.encoder['<mask>']

    def detokenizer(self, x):
        x = x.strip()
        if self.detokenize:
            x = self.md.detokenize(x.split())
            x = TreebankWordDetokenizer().detokenize(x.split())
        return x

    def encode(self, x):
        x = x.strip()
        x = self.tokenizer(x)['input_ids']
        return x


class MLMTokenizerSingleton:
    instance = None

    @classmethod
    def initialize(cls, name, detokenize):
        cls.instance = MLMTokenizer(name, detokenize)

    @classmethod
    def get(cls):
        return cls.instance


def generate_trg(token_list, index):
    tokenizer = MLMTokenizerSingleton.get()
    trg = [n for n in token_list]
    original_token = trg[index]
    trg[index] = tokenizer.mask_id
    trg = tuple(trg)
    return trg, original_token

class GeneratedSentence:
    def __init__(self, sent):
        self.text = sent['text']
        self.score = sent['score']
        tokenizer = MLMTokenizerSingleton.get()
        if tokenizer.detokenize:
            self.detokenized_text = MLMTokenizerSingleton.get(self.text)
            self.encoded_tokens = tokenizer.encode(self.detokenized_text)
        else:
            self.detokenized_text = None
            self.encoded_tokens = tokenizer.encode(self.text)
        self.mlm_score = None

    def calc_score(self, sent_dict):
        score_list = []
        for index in range(1, len(self.encoded_tokens) - 1):
            trg, original_token = generate_trg(self.encoded_tokens, index)
            score = sent_dict.sentence_dict[trg].predictions[original_token]
            score_list.append(score)
        score = sum(score_list)
        penalty = (5 + len(score_list)) / (5 + 1)
        score = score / penalty
        self.mlm_score = score


class Output(list):
    def __init__(self, f):
        lst = [[GeneratedSentence(sent) for sent in beam] for beam in yaml.safe_load(f)]
        super().__init__(lst)

    def make_sentence_dict(self):
        sent_dict = MaskedSentenceDict()
        for beam in self:
            for sent in beam:
                for index in range(1, len(sent.encoded_tokens) - 1):
                    sent_dict.add(sent.encoded_tokens, index)
        return sent_dict


class MaskedSentence:
    def __init__(self, token_list, mask_index, original_token):
        self.token_list = token_list
        self.mask_index = mask_index
        self.masked_tokens = set([original_token])
        self.predictions = {}

    def __lt__(self, other):
        return (-len(self.token_list), self.token_list) < (-len(other.token_list), other.token_list)

    def __len__(self):
        return len(self.token_list)


class MaskedSentenceDict:
    def __init__(self):
        self.sentence_dict = {}

    def add(self, token_list, mask_index):
        trg, original_token = generate_trg(token_list, mask_index)
        if trg not in self.sentence_dict:
            self.sentence_dict[trg] = MaskedSentence(trg, mask_index, original_token)
        else:
            self.sentence_dict[trg].masked_tokens.add(original_token)


class BatchLoader(list):
    def __init__(self, sent_dict, max_tokens):
        self.max_tokens = max_tokens
        self.sentence_list = list(sent_dict.sentence_dict.values())
        self.sentence_list.sort()
        self.batches = self.make_batches()
        super().__init__(self.batches)

    def make_batches(self):
        batches = []
        batch = []
        acc = 0
        max_len = len(self.sentence_list[0])
        for sent in self.sentence_list:
            acc += 1
            if acc * max_len > self.max_tokens:
                batches.append(batch)
                batch = [sent]
                acc = 1
                max_len = len(sent)
            else:
                batch.append(sent)
        if batch:
            batches.append(batch)
        return batches


class MLMScorer:
    def __init__(self, arch):
        self.model = AutoModelForMaskedLM.from_pretrained(arch)
        self.model.eval()
        self.model.cuda()
        self.pad_id = MLMTokenizerSingleton.get().pad_id

    def predict(self, batch):
        max_len = len(batch[0])
        lst = [list(sent.token_list) + [self.pad_id] * (max_len - len(sent.token_list)) for sent in batch]
        msk = [[1] * len(sent.token_list) + [0] * (max_len - len(sent.token_list)) for sent in batch]
        ten = torch.tensor(lst).cuda()
        msk = torch.tensor(msk).cuda()
        with torch.no_grad():
            out = self.model(ten, attention_mask = msk)[0]
        for logit, sent in zip(out, batch):
            dist = torch.log_softmax(logit[sent.mask_index], dim=-1)
            for n in sent.masked_tokens:
                sent.predictions[n] = dist[n].item()
        return batch


def predict_mlm_score(loader, scorer):
    for batch in tqdm(loader):
        scorer.predict(batch)


def calculate_mlm_score(output, sent_dict):
    for beam in output:
        for sent in beam:
            sent.calc_score(sent_dict)


def output_yaml(output):
    lst = []
    for beam in output:
        inner = []
        for sent in beam:
            x = {'text': sent.text, 'score': sent.score, 'detokenized_text': sent.detokenized_text, 'mlm_score': sent.mlm_score}
            inner.append(x)
        lst.append(inner)
    yml = yaml.safe_dump(lst)
    print(yml)


def mlm_scoring(arch, detokenize, max_tokens):
    MLMTokenizerSingleton.initialize(arch, detokenize)
    output = Output(sys.stdin)
    sent_dict = output.make_sentence_dict()
    loader = BatchLoader(sent_dict, max_tokens)
    scorer = MLMScorer(arch)

    predict_mlm_score(loader, scorer)
    calculate_mlm_score(output, sent_dict)
    return output


def main():
    parser = ArgumentParser()
    parser.add_argument('--arch', default='distilroberta-base')
    parser.add_argument('--detokenize', action='store_true')
    parser.add_argument('--max-tokens', type=int, default=4000)
    args = parser.parse_args()

    output = mlm_scoring(args.arch, args.detokenize, args.max_tokens)
    output_yaml(output)

