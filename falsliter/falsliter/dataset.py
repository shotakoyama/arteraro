import torch
from .vocabulary import Vocabulary

class Dataset:
    def __init__(self, src, trg):
        self.src = src
        self.trg = trg
        self.vocab = Vocabulary()
        self.size = len(self.trg)

    def __len__(self):
        return self.size

    def __call__(self, indices):
        return {'src':self.src[indices], 'trg':self.trg[indices]}

