from arteraro.erarigilo.util import *

class ColonChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('colon',
                ['', '.', ',', ';'],
                p = [0.4, 0.2, 0.2, 0.2])

    def cond(self, token):
        return token.cor == ':'


class SemiColonChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('semicolon',
                ['', '.', ',', ':'],
                p = [0.4, 0.2, 0.2, 0.2])

    def cond(self, token):
        return token.cor == ';'


@register('colon')
def _colon(dct):
    generator = TokenWiseGenerator(ColonChoiceSamplingTokenWiseMistaker)
    return generator(dct)

@register('semicolon')
def _semicolon(dct):
    generator = TokenWiseGenerator(SemiColonChoiceSamplingTokenWiseMistaker)
    return generator(dct)

