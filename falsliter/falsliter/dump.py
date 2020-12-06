from falsliter.vocabulary import Vocabulary
from falsliter.task import Task

from argparse import ArgumentParser
from itertools import product
from more_itertools import chunked

import torch
import numpy as np
from tqdm import tqdm

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('load_path')
    parser.add_argument('save_path')
    parser.add_argument('--batch-size', type = int, default = 16384)
    return parser.parse_args()

def make_score_array(n, v_size, save_path):
    score = np.memmap(save_path,
            dtype = np.float32,
            mode = 'w+',
            shape = tuple([v_size] * (2 * n + 1)))
    return score

def calc_score(model, batch, device):
    batch = torch.tensor([list(x) for x in batch], device = device)
    with torch.no_grad():
        batch = model({'src':batch})
    batch = batch.detach().cpu().numpy()
    return batch

def main():
    args = parse_args()

    vocab = Vocabulary()
    dv = len(vocab)
    dct = torch.load(args.load_path, map_location='cpu')
    n = dct['n']
    task = Task(n, dv)
    model = task.model()
    model = torch.nn.DataParallel(model)
    model.load_state_dict(dct['model'])
    model.eval()

    device = torch.device('cuda')
    model.to(device)

    score = make_score_array(n, dv, args.save_path)
    indices = product(*[range(dv) for _ in range(2 * n)])
    for batch in tqdm(chunked(indices, args.batch_size)):
        output = calc_score(model, batch, device)
        for index, dist in zip(batch, output):
            score[index] = dist

