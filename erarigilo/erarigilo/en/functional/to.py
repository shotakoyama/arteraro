from erarigilo.util import *

class ToChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('to', ['', 'by', 'for'], p = [0.6, 0.2, 0.2])

    def cond(self, token):
        return token.tag == 'TO' and token.lower == 'to'

@register('to')
def _to(dct):
    generator = TokenWiseGenerator(ToChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

