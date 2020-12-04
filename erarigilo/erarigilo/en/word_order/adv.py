import random as rd
from erarigilo.util import *

def extract_adv(sent):
    i = 0
    wh_list = []
    for i in range(len(sent)):
        if sent[i].pos == 'ADV':
            wh_list.append(i)
    return wh_list


class AdvWOMistaker(Mistaker):
    def __init__(self, scale):
        super().__init__('adv_wo')
        self.sampler = NormalSampler(loc = 0.0, scale = scale)

    def mistake(self, sent, index):
        shift = round(self.sampler())
        if 0 <= index + shift < len(sent):
            sent[index].shift += shift
            for token in sent[index].addition:
                token.shift += shift
        return sent

    def __call__(self, doc, index):
        doc = self.mistake(doc, index)
        doc[index] = self.add_history(doc[index])
        return doc


class AdvWOApplier:
    def apply(self, sent, lottery):
        adv_list = extract_adv(sent)
        for index in adv_list:
            if lottery():
                sent = self.mistaker(sent, index)
        return sent


class AdvWOManager(AdvWOApplier, BetaManager):
    pass


class AdvWOGenerator(Generator):
    def __call__(self, dct):
        mean = dct['mean']
        std = dct['std']
        scale = dct['scale']
        mistaker = self.mistaker_class(scale)
        manager = AdvWOManager(mean, std, mistaker)
        return manager


@register('adv_wo')
def _adv_wo(dct):
    generator = AdvWOGenerator(AdvWOMistaker)
    return generator(dct)

