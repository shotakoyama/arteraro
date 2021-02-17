from arteraro.erarigilo.util import *
from arteraro.erarigilo.en.util.token import EnToken

class CommaChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('comma',
                ['', '.', '. .', ';'],
                p = [0.90, 0.05, 0.025, 0.025])

    def cond(self, token):
        return token.cor == ','


class LeftSideCommaInsertingIndexWiseMistaker(ChoiceSamplingIndexWiseMistaker):
    def __init__(self):
        super().__init__('ins_left_comma',
                [',', ', ,', '.', ';', ':'],
                p = [0.9, 0.025, 0.025, 0.025, 0.025])

    def left_cond1(self, sent, index):
        return (sent[index - 1].tag in {'NN', 'NNS', 'NNP', 'NNPS'}
                or (sent[index - 1].tag in {'RB', 'RBR', 'RBS'}
                    and sent[index - 1].pos == 'ADV'))

    def cent_cond1(self, sent, index):
        return sent[index].tag in {'CC', 'DT', 'IN', 'WDT', 'WP', 'WP$', 'WRB'}

    def left_cond2(self, sent, index):
        return sent[index - 1].tag in {'NN', 'NNS', 'NNP', 'NNPS'}

    def cent_cond2(self, sent, index):
        return sent[index].tag in {'RB', 'RBR', 'RBS'} and sent[index].pos == 'ADV'

    def cond(self, sent, index):
        if 0 < index < len(sent):
            return ((self.left_cond1(sent, index) and self.cent_cond1(sent, index))
                    or (self.left_cond2(sent, index) and self.cent_cond2(sent, index)))
        return False

    def mistake(self, sent, index):
        sent[index].addition = [
                EnToken(
                    index = sent[index].index - 0.5,
                    org = self.sampler())
                ] + sent[index].addition
        return sent


class RightSideCommaInsertingIndexWiseMistaker(ChoiceSamplingIndexWiseMistaker):
    def __init__(self):
        super().__init__('ins_right_comma',
                [',', ', ,', '.', ';', ':'],
                p = [0.9, 0.025, 0.025, 0.025, 0.025])

    def centr_cond1(self, sent, index):
        return (sent[index].tag in {'NN', 'NNS', 'NNP', 'NNPS'}
                or (sent[index].tag in {'RB', 'RBR', 'RBS'}
                    and sent[index].pos == 'ADV'))

    def right_cond1(self, sent, index):
        return sent[index + 1].tag in {'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

    def cond(self, sent, index):
        if index < len(sent) - 1:
            return self.centr_cond1(sent, index) and self.right_cond1(sent, index)
        return False

    def mistake(self, sent, index):
        sent[index].addition.append(
                EnToken(
                    index = sent[index].index + 0.5,
                    org = self.sampler()))
        return sent


@register('comma')
def _comma(dct):
    generator = TokenWiseGenerator(CommaChoiceSamplingTokenWiseMistaker)
    return generator(dct)

@register('ins_left_comma')
def _ins_left_comma(dct):
    generator = IndexWiseGenerator(LeftSideCommaInsertingIndexWiseMistaker)
    return generator(dct)

@register('ins_right_comma')
def _ins_right_comma(dct):
    generator = IndexWiseGenerator(RightSideCommaInsertingIndexWiseMistaker)
    return generator(dct)

