from arteraro.erarigilo.util import *

class ThatChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_that', ['which', 'who', 'how', 'what'])

    def cond(self, token):
        return token.lower == 'that' and token.tag == 'WDT'


@register('int_that')
def _int_that(dct):
    generator = TokenWiseGenerator(ThatChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

