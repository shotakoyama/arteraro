from falsliter.vocabulary import Vocabulary
from argparse import ArgumentParser
import numpy as np
import torch
from itertools import product
from more_itertools import chunked
from tqdm import tqdm

def load_score_list(n, dv, model_path_list):
    return [np.memmap(model_path,
        dtype = np.float32,
        mode = 'r+',
        shape = tuple([dv] * (2 * n + 1)))
        for model_path in model_path_list]

def make_score_array(n, dv, save_path):
    return np.memmap(save_path,
            dtype = np.float32,
            mode = 'w+',
            shape = tuple([dv] * (2 * n + 1)))

def merge_dist(score_list, a, b, c):
    dist = torch.stack([torch.from_numpy(score[a, b, c]) for score in score_list])
    dist = torch.softmax(dist, dim=-1)
    dist = torch.mean(dist, dim=0)
    dist = torch.log(dist + 1e-40) # so that value is not -inf
    dist = dist.numpy()
    return dist

def main():
    parser = ArgumentParser()
    parser.add_argument('n', type = int)
    parser.add_argument('load_path_list')
    parser.add_argument('save_path')
    args = parser.parse_args()

    vocab = Vocabulary()
    score_list = load_score_list(args.n, len(vocab), args.load_path_list.split(':'))
    merged_score = make_score_array(args.n, len(vocab), args.save_path)

    for a, b, c in tqdm(product(range(len(vocab)), range(len(vocab)), range(len(vocab)))):
        merged_score[a, b, c] = merge_dist(score_list, a, b, c)

