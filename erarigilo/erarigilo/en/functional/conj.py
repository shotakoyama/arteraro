from erarigilo.util import *

class AndChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('conj_and',
                ['', 'but'],
                p = [0.95, 0.05])

    def cond(self, token):
        return token.lower == 'and'


class ButChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('conj_but',
                ['', 'and'],
                p = [0.9, 0.1])

    def cond(self, token):
        return token.lower == 'but'


@register('conj_and')
def _conj_and(dct):
    generator = TokenWiseGenerator(AndChoiceSamplingTokenWiseMistaker)
    return generator(dct)

@register('conj_but')
def _conj_but(dct):
    generator = TokenWiseGenerator(ButChoiceSamplingTokenWiseMistaker)
    return generator(dct)

