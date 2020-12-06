from erarigilo.util import *

class NormWOMistaker(Mistaker):
    def __init__(self, loc, scale):
        super().__init__('norm_wo')
        self.sampler = NormalSampler(loc, scale)

    def __call__(self, ratio, token):
        token.shift += ratio * self.sampler()
        token = self.add_history(token)
        return token


class NormWOManager(Manager):
    def __init__(self, mean, std, mistaker):
        super().__init__(mistaker)
        self.beta_sampler = BetaSampler(mean, std)

    def __call__(self, sent):
        ratio = self.beta_sampler()
        for i in range(len(sent)):
            sent[i] = self.mistaker(ratio, sent[i])
        sent.history.append({'name' : self.mistaker.name, 'ratio' : round(ratio, 2)})
        return sent


class NormWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        loc = dct['loc']
        scale = dct['scale']
        mistaker = NormWOMistaker(loc, scale)
        manager = NormWOManager(mean, std, mistaker)
        return manager


@register('norm_wo')
def _norm_wo(dct):
    generator = NormWOGenerator(NormWOMistaker)
    return generator(dct)

