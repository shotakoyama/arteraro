from erarigilo.util import *
from erarigilo.en.util.token import EnToken

class DeterminerInsertingChoiceSamplingIndexWiseMistaker(ChoiceSamplingIndexWiseMistaker):
    def __init__(self):
        super().__init__('ins_det',
                ['a', 'an', 'the', 'this', 'that', 'these', 'those'],
                p = [0.3, 0.3, 0.3, 0.025, 0.025, 0.025, 0.025])

    def cond(self, sent, index):
        return ((index == 0
            and sent[index].tag in {'NN', 'NNS', 'JJ', 'JJN', 'JJS'})
            or
            (0 < index < len(sent)
                and sent[index - 1].tag in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'IN'}
                and sent[index].tag in {'NN', 'NNS', 'JJ', 'JJN', 'JJS'}))

    def mistake(self, sent, index):
        if index == 0:
            if sent[index].org is None:
                sent[index].org = sent[index].cor
            sent[index].org = sent[index].org.lower()

        cand = self.sampler()
        if index == 0:
            cand = cand.title()

        sent[index].addition = [
                EnToken(
                    index = sent[index].index - 0.5,
                    org = cand)
                ] + sent[index].addition
        return sent


@register('ins_det')
def _ins_det(dct):
    generator = IndexWiseGenerator(DeterminerInsertingChoiceSamplingIndexWiseMistaker)
    return generator(dct)

