from erarigilo.util import *

class WhetherChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whether', ['which', 'what', 'that', 'how', 'whatever', 'whatsoever', 'if'])

    def cond(self, token):
        return token.lower == 'whether'


@register('int_whether')
def _int_whether(dct):
    generator = TokenWiseGenerator(WhetherChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

