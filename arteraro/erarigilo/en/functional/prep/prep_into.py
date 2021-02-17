from arteraro.erarigilo.util import *
from .generator import *

@register('prep_into')
def _prep_into(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_into',
            word_set = {'into'},
            choice_list = ['', 'in', 'to', 'toward', 'towards'],
            p = [0.2, 0.3, 0.3, 0.1, 0.1])

