import os
import torch
from tqdm import tqdm
from logging import getLogger
logger = getLogger(__name__)

class Trainer:
    def __init__(self, model, loader, task, optimizer, max_iter, device = None):
        self.model = model.to(device)
        self.loader = loader
        self.task = task
        self.optimizer = optimizer
        self.max_iter = max_iter
        self.device = device

    def send(self, batch):
        for key in batch:
            batch[key] = batch[key].to(self.device)
        return batch

    def save(self, epoch):
        os.makedirs('checkpoints', exist_ok=True)
        path = f'checkpoints/checkpoint{epoch}.pt'
        dct = {'epoch':epoch}
        dct.update(self.task.save(self.model))
        torch.save(dct, path)

    def train_epoch(self):
        self.model.train()
        train_loss = 0.0
        examples = 0
        for n, batch in enumerate(tqdm(self.loader, bar_format='{l_bar}{r_bar}', leave=False)):
            batch = self.send(batch)
            loss = self.task.train_step(self.model, batch)
            train_loss += loss * len(batch)
            examples += len(batch)
            self.optimizer.step()
        return train_loss / examples

    def train(self):
        for epoch in range(self.max_iter):
            train_loss = self.train_epoch()
            self.save(epoch)
            logger.info('epoch {}, train_loss:{:.5f}'.format(epoch, train_loss))

