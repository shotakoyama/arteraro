from .sampler import *
from .applier import *

class Manager:
    def __init__(self, mistaker):
        self.mistaker = mistaker

    def __call__(self, sent):
        sent = self.noise(sent)
        sent.history.append({'name' : self.mistaker.name})
        return sent


class BetaManager(Manager):
    def __init__(self, mean, std, mistaker):
        super().__init__(mistaker)
        self.uniform_sampler = UniformSampler()
        self.beta_sampler = BetaSampler(mean, std)

    def get_threshold(self):
        threshold = self.beta_sampler()
        return threshold

    def __call__(self, sent):
        threshold = self.get_threshold()
        lottery = lambda : self.uniform_sampler() < threshold
        sent = self.apply(sent, lottery)
        sent.history.append({'name' : self.mistaker.name, 'threshold' : round(threshold, 2)})
        return sent


class TokenWiseBetaManager(TokenWiseApplier, BetaManager):
    pass


class IndexWiseBetaManager(IndexWiseApplier, BetaManager):
    pass


class SpanWiseBetaManager(SpanWiseApplier, BetaManager):
    pass

