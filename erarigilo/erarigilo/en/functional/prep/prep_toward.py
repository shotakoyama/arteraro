from erarigilo.util import *
from .generator import *

@register('prep_toward')
def _prep_toward(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_toward',
            word_set = {'toward', 'towards'},
            choice_list = ['to', 'with', 'of', 'for', 'in', 'into'])

