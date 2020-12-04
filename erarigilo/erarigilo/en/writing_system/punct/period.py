from erarigilo.util import *

class PeriodChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('period',
                ['', ',', '. .', '..', ':', ';', '!', '?'],
                p = [0.5, 0.3, 0.05, 0.05, 0.025, 0.025, 0.025, 0.025])

    def cond(self, token):
        return token.cor == '.'


@register('period')
def _period(dct):
    generator = TokenWiseGenerator(PeriodChoiceSamplingTokenWiseMistaker)
    return generator(dct)

