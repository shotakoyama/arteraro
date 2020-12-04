from erarigilo.util import *

class WhoseChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('int_whose', ['which', 'who', 'that', 'its', 'his', 'her', 'their'])

    def cond(self, token):
        return token.lower == 'whose'


@register('int_whose')
def _int_whose(dct):
    generator = TokenWiseGenerator(WhoseChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)
