from arteraro.erarigilo.util import *

class WhitherChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whither', ['when', 'whence', 'that', 'what'])

    def cond(self, token):
        return token.lower == 'whither'


@register('int_whither')
def _int_whither(dct):
    generator = TokenWiseGenerator(WhitherChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

