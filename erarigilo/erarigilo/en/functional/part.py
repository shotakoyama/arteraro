from erarigilo.util import *

class ParticleChoiceSamplingTokenWiseMistaker(ChoiceSamplingTokenWiseMistaker):
    def __init__(self):
        super().__init__('part',
                ['', 'out', 'up', 'down', 'about', 'on', 'in', 'off'],
                p = [0.65] + [0.05] * 7)

    def cond(self, token):
        return token.dep == 'prt' and token.tag == 'RP'


@register('part')
def _part(dct):
    generator = TokenWiseGenerator(ParticleChoiceSamplingTokenWiseMistaker)
    return generator(dct)

