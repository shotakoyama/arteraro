from erarigilo.util import *
from .generator import *

@register('dative_to')
def _dative_to(dct):
    return generate_sampling_dative_generator(dct,
            name = 'dative_to',
            word_set = {'to'},
            choice_list = ['', 'for'],
            p = [0.4, 0.6])

@register('dative_for')
def _dative_for(dct):
    return generate_sampling_dative_generator(dct,
            name = 'dative_for',
            word_set = {'for'},
            choice_list = ['', 'to'],
            p = [0.4, 0.6])

