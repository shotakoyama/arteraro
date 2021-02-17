from arteraro.erarigilo.util import *
from arteraro.erarigilo.en.util.token import EnToken

class HyphenChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('hyphen',
                ['', '--', '---', '- -'],
                p = [0.85, 0.10, 0.025, 0.025])

    def cond(self, token):
        return token.cor == '-'


class TwoHyphensChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('two_hyphens',
                ['', '-', '---', '- -'],
                p = [0.2, 0.7, 0.05, 0.05])

    def cond(self, token):
        return token.cor == '--'


class HyphenInsertingIndexWiseMistaker(ChoiceSamplingIndexWiseMistaker):
    def __init__(self):
        super().__init__('ins_hyphen',
                ['-', '--', '---', '- -'],
                p = [0.7, 0.25, 0.025, 0.025])

    def c1(self, sent, index):
        return sent[index].tag in {'JJ','JJR', 'JJS', 'NN', 'NNS', 'RB', 'CD'}

    def r1(self, sent, index):
        return sent[index + 1].tag in {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'VBN', 'VBG'}

    def c2(self, sent, index):
        return sent[index].tag in {'JJ', 'JJR', 'JJS', 'CD', 'NN', 'NNS'}

    def r2(self, sent, index):
        return sent[index + 1].tag == 'RB'

    def c3(self, sent, index):
        return sent[index].tag == 'CD'

    def r3(self, sent, index):
        return sent[index + 1].tag == 'CD'

    def c4(self, sent, index):
        return sent[index].tag in {'VB', 'VBG', 'VBN', 'NN', 'NNS'}

    def r4(self, sent, index):
        return sent[index + 1].tag == 'RP'

    def cond(self, sent, index):
        if index < len(sent) - 1:
            return ((self.c1(sent, index) and self.r1(sent, index))
                    or (self.c2(sent, index) and self.r2(sent, index))
                    or (self.c3(sent, index) and self.r3(sent, index))
                    or (self.c4(sent, index) and self.r4(sent, index)))
        return False

    def mistake(self, sent, index):
        sent[index].addition.append(
                EnToken(
                    index = sent[index].index + 0.5,
                    org = self.sampler()))
        return sent

@register('hyphen')
def _hyphen(dct):
    generator = TokenWiseGenerator(HyphenChoiceSamplingTokenWiseMistaker)
    return generator(dct)

@register('two_hyphens')
def _two_hyphens(dct):
    generator = TokenWiseGenerator(TwoHyphensChoiceSamplingTokenWiseMistaker)
    return generator(dct)

@register('ins_hyphen')
def _ins_hyphen(dct):
    generator = IndexWiseGenerator(HyphenInsertingIndexWiseMistaker)
    return generator(dct)

