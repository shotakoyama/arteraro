import torch
import torch.nn as nn
from .model import FalsLiterModel

class Task:
    def __init__(self, n_size, v_size):
        self.criterion = nn.CrossEntropyLoss()
        self.n_size = n_size
        self.v_size = v_size

    def model(self):
        return FalsLiterModel(self.n_size, self.v_size)

    def train_step(self, model, batch):
        model.zero_grad()
        loss = self.criterion(model(batch).view(-1, self.v_size), batch['trg'])
        loss.backward()
        return loss.item()

    def save(self, model):
        return {'n':self.n_size, 'model':model.state_dict()}

