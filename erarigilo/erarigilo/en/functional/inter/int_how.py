from erarigilo.util import *

class HowChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_how', ['what', 'that', 'who', 'which'], p = [0.6, 0.2, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'how'

@register('int_how')
def _int_how(dct):
    generator = TokenWiseGenerator(HowChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

