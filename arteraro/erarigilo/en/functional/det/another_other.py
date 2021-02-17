from arteraro.erarigilo.util import *
from .mistaker import *

class OtherChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('other', ['another', 'others'])

    def cond(self, token):
        return token.lower == 'other'


@register('another')
def _another(dct):
    generator = ChoiceSamplingTokenWiseGenerator(DeterminerChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct,
            name = 'another',
            word_cond = lambda token : token.lower == 'another',
            choice_list = ['other', 'the other', 'an other'])

@register('other')
def _other(dct):
    generator = TokenWiseGenerator(OtherChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

