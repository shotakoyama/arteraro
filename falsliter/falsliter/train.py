from falsliter.dataset import Dataset
from falsliter.loader import Loader
from falsliter.task import Task
from falsliter.trainer import Trainer

from argparse import ArgumentParser
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

import sys
import logging
from logging import getLogger, Formatter, StreamHandler
logger = getLogger(__name__)
logging.basicConfig(format='[%(asctime)s] (%(levelname)s) %(message)s', datefmt='%Y/%m/%d %H:%M:%S', level=logging.DEBUG, stream=sys.stdout)

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('trg')
    parser.add_argument('--batch-size', type = int, default = 1024 * 1024)
    parser.add_argument('--max-epoch', type = int, default = 100)
    args = parser.parse_args()
    return args

def load_dataset(args):
    src = torch.tensor(np.load(args.src))
    trg = torch.tensor(np.load(args.trg))
    n = src.shape[-1] // 2
    dataset = Dataset(src, trg)
    return n, dataset

def main():
    args = parse_args()
    n, dataset = load_dataset(args)
    loader = Loader(dataset, args.batch_size)
    task = Task(n, len(dataset.vocab))
    model = task.model()
    model = nn.DataParallel(model)
    optimizer = optim.AdamW(model.parameters(), lr=2e-3)
    device = torch.device('cuda')
    trainer = Trainer(model, loader, task, optimizer, args.max_epoch, device)
    trainer.train()

