from erarigilo.util import *

class NormWOMistaker(Mistaker):
    def __init__(self):
        super().__init__('norm_wo')
        self.sampler = NormalSampler(0, 1)

    def __call__(self, ratio, token):
        token.shift += ratio * self.sampler()
        token = self.add_history(token)
        return token


class NormWOManager(Manager):
    def __init__(self, sent_ratio, loc, scale, mistaker):
        super().__init__(mistaker)
        self.sent_ratio = sent_ratio
        self.uniform_sampler = UniformSampler()
        self.ratio_sampler = NormalSampler(loc, scale)

    def apply(self, sent):
        if self.uniform_sampler() < self.sent_ratio:
            ratio = self.ratio_sampler()
            for i in range(len(sent)):
                sent[i] = self.mistaker(ratio, sent[i])
        return sent

    def __call__(self, sent):
        sent = self.apply(sent)
        sent.history.append({'name' : self.mistaker.name, 'ratio' : round(self.sent_ratio, 2)})
        return sent


class NormWOGenerator(Generator):
    def __call__(self, dct):
        sent_ratio = dct['sent_ratio']
        loc = dct['loc']
        scale = dct['scale']
        mistaker = NormWOMistaker()
        manager = NormWOManager(sent_ratio, loc, scale, mistaker)
        return manager


@register('norm_wo')
def _norm_wo(dct):
    generator = NormWOGenerator(NormWOMistaker)
    return generator(dct)

