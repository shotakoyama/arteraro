from .vocabulary import Vocabulary
import numpy as np
import torch

class FalsLiterNoiser:
    def __init__(self, n, score_path, temp=1.0):
        self.vocab = Vocabulary()
        self.n = n
        self.score = np.memmap(score_path,
                dtype = np.float32,
                mode = 'r',
                shape = tuple([len(self.vocab)] * (2 * n + 1)))
        self.temp = temp

    def get_dist(self, src, trg):
        src = tuple(self.vocab.index(char) for char in src)
        dist = np.array(self.score[src].tolist())
        if trg is not None:
            dist[self.vocab.index(trg)] = -float('Inf')
        dist[[0, 1]] = -float('Inf')
        dist = torch.from_numpy(dist)
        dist = dist / self.temp
        dist = torch.softmax(dist, dim=-1)
        dist = dist.numpy()
        return dist

    def __call__(self, src, trg = None):
        if len(src) != 2 * self.n:
            raise RuntimeError

        dist = self.get_dist(src, trg)
        cand_id = np.random.choice(range(len(self.vocab)), p = dist)
        cand = self.vocab[cand_id]
        return cand

