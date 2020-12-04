from erarigilo.util import *

class ThereChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('there', ['', 'here', 'they', 'it'], p = [0.5, 0.3, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'there'


class HereChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('here', ['', 'there', 'they', 'it'], p = [0.5, 0.3, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'here'


@register('there')
def _there(dct):
    generator = TokenWiseGenerator(ThereChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('here')
def _here(dct):
    generator = TokenWiseGenerator(HereChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

