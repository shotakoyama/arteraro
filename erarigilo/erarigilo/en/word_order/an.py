import random as rd
from erarigilo.util import *

class AN:
    def __init__(self, a_list, n_list):
        self.a_list = a_list
        self.n_list = n_list

    def check(self, sent):
        for i in self.a_list + self.n_list:
            if not sent[i].word().isalnum():
                return False
        return True


def extract_an(sent):
    i = 0
    an_list = []
    while i < len(sent):
        if sent[i].tag in {'JJ', 'JJR', 'JJS', 'CD'}:
            a_list = [i]
            i += 1
            while i < len(sent) and sent[i].tag in {'JJ', 'JJR', 'JJS', 'CD'}:
                a_list.append(i)
                i += 1
            n_list = []
            while i < len(sent) and sent[i].tag in {'NN', 'NNS'}:
                n_list.append(i)
                i += 1
            an = AN(a_list, n_list)
            if an.check(sent):
                an_list.append(an)
        i += 1
    return an_list


class ANWOMistaker(Mistaker):
    def __init__(self, ratio):
        super().__init__('an_wo')
        self.ratio = ratio
        self.sampler = UniformSampler()

    def mistake(self, sent, a_list, n_list, prop):
        a_shift = a_list.copy()
        n_shift = [0 for _ in n_list]
        rd.shuffle(a_shift)
        a_shift = [x - y for x, y in zip(a_shift, a_list)]
        if prop:
            a_shift = [x + len(n_list) for x in a_shift]
            n_shift = [x - len(a_list) for x in n_shift]
        for i, shift in zip(a_list + n_list, a_shift + n_shift):
            sent[i].shift += shift
            for token in sent[i].addition:
                token.shift += shift
        return sent

    def __call__(self, sent, a_list, n_list):
        prop = self.sampler() < self.ratio
        sent = self.mistake(sent, a_list, n_list, prop)
        for index in a_list + n_list:
            sent[index] = self.add_history(sent[index])
        return sent


class ANWOApplier:
    def apply(self, sent, lottery):
        an_list = extract_an(sent)
        for an in an_list:
            if lottery():
                sent = self.mistaker(sent, an.a_list, an.n_list)
        return sent


class ANWOManager(ANWOApplier, BetaManager):
    pass


class ANWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        ratio = dct['ratio']
        mistaker = self.mistaker_class(ratio)
        manager = ANWOManager(mean, std, mistaker)
        return manager


@register('an_wo')
def _an_wo(dct):
    generator = ANWOGenerator(ANWOMistaker)
    return generator(dct)

