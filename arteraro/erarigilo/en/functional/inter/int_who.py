from arteraro.erarigilo.util import *

class WhoChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_who', ['that', 'which', 'what', 'how'], p = [0.3, 0.3, 0.2, 0.2])

    def cond(self, token):
        return token.lower == 'who'


class WhoeverChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whoever', ['whatever', 'whichever', 'however', 'who'])

    def cond(self, token):
        return token.lower == 'whoever'


@register('int_who')
def _int_who(dct):
    generator = TokenWiseGenerator(WhoChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('int_whoever')
def _int_whoever(dct):
    generator = TokenWiseGenerator(WhoeverChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

