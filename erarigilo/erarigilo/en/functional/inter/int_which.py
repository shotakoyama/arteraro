from erarigilo.util import *

class WhichChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_which', ['that', 'who', 'what', 'how'], p = [0.3, 0.3, 0.2, 0.2])

    def cond(self, token):
        return token.lower == 'which'


class WhicheverChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whichever', ['whatever', 'whoever', 'however', 'which'])

    def cond(self, token):
        return token.lower == 'whichever'


@register('int_which')
def _int_which(dct):
    generator = TokenWiseGenerator(WhichChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('int_whichever')
def _int_whichever(dct):
    generator = TokenWiseGenerator(WhicheverChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

