from arteraro.erarigilo.util import *
from .generator import *

@register('prep_during')
def _prep_during(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_during',
            word_set = {'during'},
            choice_list = ['in', 'for', 'while', 'when', 'through', 'across'])

