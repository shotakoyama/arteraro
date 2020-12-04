from erarigilo.util import *

class AuxpassReplacingTokenWiseMistaker(ReplacingTokenWiseMistaker):
    def __init__(self):
        super().__init__('auxpass', '')

    def cond(self, token):
        return token.dep == 'auxpass'


@register('auxpass')
def _auxpass(dct):
    generator = TokenWiseGenerator(AuxpassReplacingTokenWiseMistaker)
    return generator(dct)

