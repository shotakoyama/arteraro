from arteraro.erarigilo.util import *

class WhereChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_where', ['when', 'wherein', 'whereas', 'whereby'])

    def cond(self, token):
        return token.lower == 'where'


class WhereverChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_wherever', ['where', 'whatever', 'whenever', 'whichever', 'wherein', 'whereas', 'whereby'])

    def cond(self, token):
        return token.lower == 'wherever'


@register('int_where')
def _int_where(dct):
    generator = TokenWiseGenerator(WhereChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

@register('int_wherever')
def _int_wherever(dct):
    generator = TokenWiseGenerator(WhereverChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

