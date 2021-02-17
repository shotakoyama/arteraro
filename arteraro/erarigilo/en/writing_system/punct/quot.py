from arteraro.erarigilo.util import *

class QuotChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        lst = ['', "'", '"', "''", '``']
        super().__init__('quot', lst)

    def cond(self, token):
        return token.tag in {'``', "''"}


@register('quot')
def _quot(dct):
    generator = TokenWiseGenerator(QuotChoiceSamplingTokenWiseMistaker)
    return generator(dct)

