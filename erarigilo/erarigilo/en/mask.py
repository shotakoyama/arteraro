from erarigilo.util import *
import random as rd

mask = chr(0x25a8)

class MaskMistaker(TokenWiseMistaker):
    def __init__(self):
        super().__init__('mask')

    def cond(self, token):
        return token.word() != ''

    def noise(self, token):
        token.org = mask
        return token

    def __call__(self, token):
        token = self.noise(token)
        token = self.add_history(token)
        return token


class BetterMaskMistaker(MaskMistaker):
    def __init__(self, threshold_mean, threshold_std):
        super().__init__()
        self.beta_sampler = BetaSampler(threshold_mean, threshold_std)
        self.uniform_sampler = UniformSampler()

    def noise(self, token, thres):
        if self.uniform_sampler() < thres:
            word = token.word()
            lst = rd.sample(range(len(word) + 1), k = 2)
            lst.sort()
            start, end = lst
            token.org = word[:start] + mask + word[end:]
        else:
            token.org = mask
        return token

    def __call__(self, token, thres):
        token = self.noise(token, thres)
        token = self.add_history(token)
        return token


class MaskApplier:
    def apply(self, sent, lottery):
        # apply mask mistakes
        for index in range(len(sent)):

            # apply for original tokens
            if self.mistaker.cond(sent[index]) and lottery():
                sent[index] = self.mistaker(sent[index])

            # apply for added tokens
            for pos in range(len(sent[index].addition)):
                if self.mistaker.cond(sent[index].addition[pos]) and lottery():
                    sent[index].addition[pos] = self.mistaker(sent[index].addition[pos])

        return sent


class BetterMaskApplier:
    def apply(self, sent, lottery):
        # threshold
        thres = self.mistaker.beta_sampler()

        # apply mask mistakes
        for index in range(len(sent)):

            # apply for original tokens
            if self.mistaker.cond(sent[index]) and lottery():
                sent[index] = self.mistaker(sent[index], thres)

            # apply for added tokens
            for pos in range(len(sent[index].addition)):
                if self.mistaker.cond(sent[index].addition[pos]) and lottery():
                    sent[index].addition[pos] = self.mistaker(sent[index].addition[pos], thres)

        return sent


class MaskManager(MaskApplier, TokenWiseBetaManager):
    pass


class BetterMaskManager(BetterMaskApplier, TokenWiseBetaManager):
    pass


class MaskGenerator(Generator):
    def __init__(self):
        pass

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        threshold_mean = dct.get('threshold_mean', 0.0)
        threshold_std = dct.get('threshold_std', 0.0)
        if threshold_mean == 0.0:
            mistaker = MaskMistaker()
            manager = MaskManager(mean, std, mistaker)
        else:
            mistaker = BetterMaskMistaker(threshold_mean, threshold_std)
            manager = BetterMaskManager(mean, std, mistaker)
        return manager


@register('mask')
def _mask(dct):
    generator = MaskGenerator()
    return generator(dct)

