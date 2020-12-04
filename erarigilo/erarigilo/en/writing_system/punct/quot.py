from erarigilo.util import *

class QuotChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        lst = ['', "'", '"', "''", '``'] + [chr(x) for x in range(0x2018, 0x2020)]
        p = [0.3] + [0.7 / (len(lst) - 1)] * (len(lst) - 1)
        super().__init__('quot', lst, p = p)

    def cond(self, token):
        return token.tag in {'``', "''"}


@register('quot')
def _quot(dct):
    generator = TokenWiseGenerator(QuotChoiceSamplingTokenWiseMistaker)
    return generator(dct)

