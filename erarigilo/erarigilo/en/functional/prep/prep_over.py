from erarigilo.util import *
from .generator import *

@register('prep_over')
def _prep_over(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_over',
            word_set = {'over'},
            choice_list = ['on', 'from', 'to', 'above'])

