from erarigilo.util import *
from .generator import *

@register('prep_above')
def _prep_above(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_above',
            word_set = {'above'},
            choice_list = ['on', 'from', 'to', 'over'])

