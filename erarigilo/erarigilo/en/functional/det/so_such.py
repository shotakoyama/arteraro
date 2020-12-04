from erarigilo.util import *

class SoChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('so', ['', 'such', 'too'])

    def cond(self, token):
        return token.lower == 'so'


class SuchChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('such', ['', 'so', 'very'])

    def cond(self, token):
        return token.lower == 'such'


@register('so')
def _so(dct):
    generator = TokenWiseGenerator(SoChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('such')
def _such(dct):
    generator = TokenWiseGenerator(SuchChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

