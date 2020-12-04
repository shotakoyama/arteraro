import numpy as np
from collections import deque

class Sampler:
    def __init__(self, buffer_size = None):
        self.queue = deque()
        if buffer_size is not None:
            self.buffer_size = buffer_size
        else:
            self.buffer_size = 10000

    def __call__(self):
        if not self.queue:
            self.queue.extend(self.sampler())
        return self.queue.pop()


class UniformSampler(Sampler):
    def sampler(self):
        return np.random.rand(self.buffer_size)


class NormalSampler(Sampler):
    def __init__(self, loc, scale, buffer_size = None):
        super().__init__(buffer_size = buffer_size)
        self.loc = loc
        self.scale = scale

    def sampler(self):
        return np.random.normal(loc = self.loc, scale = self.scale, size = self.buffer_size)


class BetaSampler(Sampler):
    def __init__(self, mean, std, buffer_size = None):
        super().__init__(buffer_size = buffer_size)
        self.a = mean * mean * (1. - mean) / (std ** 2) - mean
        self.b = self.a / mean - self.a

    def sampler(self):
        return np.random.beta(self.a, self.b, self.buffer_size)


class GeometricSampler(Sampler):
    def __init__(self, p, buffer_size = None):
        super().__init__(buffer_size = buffer_size)
        self.p = p

    def sampler(self):
        return np.random.geometric(self.p, self.buffer_size)


class ChoiceSampler(Sampler):
    def __init__(self, cands, p = None, buffer_size = None):
        super().__init__(buffer_size = buffer_size)
        self.cands = cands
        self.p = p

    def sampler(self):
        return np.random.choice(self.cands, size = self.buffer_size, p = self.p)

