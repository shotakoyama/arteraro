from .sampler import Sampler

class Loader:
    def __init__(self, dataset, width):
        self.dataset = dataset
        self.sampler = Sampler(dataset, width) 

    def __iter__(self):
        for indices in self.sampler:
            yield self.dataset(indices)

