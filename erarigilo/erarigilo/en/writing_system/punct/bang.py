from erarigilo.util import *

class ExclamationColonChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('bang',
                ['', '.', ',', '?'],
                p = [0.4, 0.2, 0.2, 0.2])

    def cond(self, token):
        return token.cor == '!'

@register('bang')
def _bang(dct):
    generator = TokenWiseGenerator(ExclamationColonChoiceSamplingTokenWiseMistaker)
    return generator(dct)

