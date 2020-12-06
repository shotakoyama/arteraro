from erarigilo.util import *
import random as rd

char_mask = chr(0x25a1)
word_mask = chr(0x25a8)

class MaskMistaker(TokenWiseMistaker):
    def __init__(self):
        super().__init__('mask')

    def cond(self, token):
        return token.word() != ''

    def noise(self, token):
        token.org = word_mask
        return token

    def __call__(self, token):
        token = self.noise(token)
        token = self.add_history(token)
        return token


class BetterMaskMistaker(MaskMistaker):
    def __init__(self, p, threshold_mean, threshold_std):
        super().__init__()
        self.beta_sampler = BetaSampler(threshold_mean, threshold_std)
        self.geometric_sampler = GeometricSampler(p)
        self.uniform_sampler = UniformSampler()

    def noise(self, token, thres):
        if self.uniform_sampler() < thres:
            word = token.word()
            num_iter = self.geometric_sampler()
            for _ in range(num_iter):
                if len(word) > 1:
                    pos = rd.randrange(len(word) - 1)
                    word = word[:pos] + char_mask + word[pos+1:]
            token.org = word
        else:
            token.org = word_mask
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
    def apply(self, sent, lottery, char_threshold):
        # apply mask mistakes
        for index in range(len(sent)):

            # apply for original tokens
            if self.mistaker.cond(sent[index]) and lottery():
                sent[index] = self.mistaker(sent[index], char_threshold)

            # apply for added tokens
            for pos in range(len(sent[index].addition)):
                if self.mistaker.cond(sent[index].addition[pos]) and lottery():
                    sent[index].addition[pos] = self.mistaker(sent[index].addition[pos], char_threshold)

        return sent


class MaskManager(MaskApplier, TokenWiseBetaManager):
    pass


class BetterMaskManager(BetterMaskApplier, TokenWiseBetaManager):
    def __call__(self, sent):
        word_threshold = self.get_threshold()
        char_threshold = self.mistaker.beta_sampler()
        lottery = lambda : self.uniform_sampler() < word_threshold
        sent = self.apply(sent, lottery, char_threshold)
        sent.history.append({'name' : self.mistaker.name, 'threshold' : round(word_threshold, 2), 'char_threshold' : round(char_threshold, 2)})
        return sent


class MaskGenerator(Generator):
    def __init__(self):
        pass

    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        p = dct.get('p', 0.9)
        threshold_mean = dct.get('threshold_mean', 0.0)
        threshold_std = dct.get('threshold_std', 0.0)
        if threshold_mean == 0.0:
            mistaker = MaskMistaker()
            manager = MaskManager(mean, std, mistaker)
        else:
            mistaker = BetterMaskMistaker(p, threshold_mean, threshold_std)
            manager = BetterMaskManager(mean, std, mistaker)
        return manager


@register('mask')
def _mask(dct):
    generator = MaskGenerator()
    return generator(dct)

