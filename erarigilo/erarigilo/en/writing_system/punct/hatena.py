from erarigilo.util import *

class InterrogationChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('hatena',
                ['', '.', ',', '!'],
                p = [0.1, 0.75, 0.1, 0.05])

    def cond(self, token):
        return token.cor == '?'


@register('hatena')
def _hatena(dct):
    generator = TokenWiseGenerator(InterrogationChoiceSamplingTokenWiseMistaker)
    return generator(dct)

