from erarigilo.util import *

class WhyChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_why', ['how', 'when', 'where', 'that', 'what'])

    def cond(self, token):
        return token.lower == 'why'

@register('int_why')
def _int_why(dct):
    generator = TokenWiseGenerator(WhyChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

