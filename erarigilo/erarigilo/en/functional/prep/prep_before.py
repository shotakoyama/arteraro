from erarigilo.util import *
from .generator import *

@register('prep_before')
def _prep_before(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_before',
            word_set = {'before'},
            choice_list = ['on', 'for', 'when'])

