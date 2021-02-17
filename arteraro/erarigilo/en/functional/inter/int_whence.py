from arteraro.erarigilo.util import *

class WhenceChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whence', ['when', 'whither', 'where', 'what'])

    def cond(self, token):
        return token.lower == 'whence'


@register('int_whence')
def _int_whence(dct):
    generator = TokenWiseGenerator(WhenceChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

