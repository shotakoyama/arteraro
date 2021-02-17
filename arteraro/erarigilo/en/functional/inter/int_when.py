from arteraro.erarigilo.util import *

class WhenChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_when', ['where', 'until', 'that', 'what', 'for', 'in'])

    def cond(self, token):
        return token.lower == 'when'


class WheneverChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whenever', ['when', 'whatever', 'wherever', 'whichever', 'until', 'that', 'what', 'for', 'in'])

    def cond(self, token):
        return token.lower == 'whenever'


@register('int_when')
def _int_when(dct):
    generator = TokenWiseGenerator(WhenChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('int_whenever')
def _int_whenever(dct):
    generator = TokenWiseGenerator(WheneverChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

