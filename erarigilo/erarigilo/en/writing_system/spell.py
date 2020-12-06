import random as rd
from erarigilo.util import *
from falsliter.noiser import FalsLiterNoiser
#from cboc.vocab import Vocab
#from cboc.noiser import CBOCNoiser

class WordSpellCorrupter:
    def __init__(self, char_prob, n, score_path, temp):
        self.n = n
        self.noiser = FalsLiterNoiser(n, score_path, temp)
        self.num_edit_sampler = GeometricSampler(char_prob)
        self.operation_sampler = ChoiceSampler([self.delete, self.insert, self.replace, self.swap])

    def delete(self, word):
        if len(word) <= 1:
            return word
        pos = rd.randrange(len(word))
        cand = word[:pos] + word[pos + 1:]
        return cand

    def swap(self, word):
        if len(word) <= 1:
            return word
        pos = rd.randrange(len(word) - 1)
        cand = word[:pos] + word[pos + 1] + word[pos] + word[pos + 2:]
        return cand

    def cap(self, word):
        return [self.noiser.vocab.bos] * self.n + list(word) + [self.noiser.vocab.eos] * self.n

    def insert(self, word):
        pos = rd.randrange(len(word) + 1)
        capped = self.cap(word)
        src = capped[pos : pos + self.n] + capped[pos + self.n : pos + self.n * 2]
        pred = self.noiser(src)
        return word[:pos] + pred + word[pos:]

    def replace(self, word):
        if len(word) <= 0:
            return word
        pos = rd.randrange(len(word))
        capped = self.cap(word)
        src = capped[pos : pos + self.n] + capped[pos + self.n + 1 : pos + self.n * 2 + 1]
        trg = capped[pos + self.n]
        pred = self.noiser(src, trg = trg)
        return word[:pos] + pred + word[pos + 1:]

    def __call__(self, word):
        for _ in range(self.num_edit_sampler()):
            sampler = self.operation_sampler()
            word = sampler(word)
        return word


class SpellMistaker(TokenWiseMistaker):
    def __init__(self, char_prob, n, score_path, temp):
        super().__init__('spell')
        self.corrupter = WordSpellCorrupter(char_prob, n, score_path, temp)

    def cond(self, token):
        word = token.word()
        return all(char in self.corrupter.noiser.vocab for char in word)

    def mistake(self, token):
        word = token.word()
        cand = self.corrupter(word)
        return cand


class SpellGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        char_prob = dct['char_prob']
        n = dct['n']
        score_path = replace_environment_variable(dct['score_path'])
        temp = dct['temp']
        mistaker = self.mistaker_class(char_prob, n, score_path, temp)
        manager = TokenWiseBetaManager(mean, std, mistaker)
        return manager


@register('spell')
def _spell(dct):
    generator = SpellGenerator(SpellMistaker)
    return generator(dct)

