from erarigilo.util import *

class WhatChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_what', ['how', 'that', 'which', 'who'], p = [0.6, 0.2, 0.1, 0.1])

    def cond(self, token):
        return token.lower == 'what'


class WhateverChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whatever', ['what', 'however', 'whichever', 'whoever'], p = [0.4, 0.2, 0.2, 0.2])

    def cond(self, token):
        return token.lower == 'whatever'


@register('int_what')
def _int_what(dct):
    generator = TokenWiseGenerator(WhatChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('int_whatever')
def _int_whatever(dct):
    generator = TokenWiseGenerator(WhateverChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

