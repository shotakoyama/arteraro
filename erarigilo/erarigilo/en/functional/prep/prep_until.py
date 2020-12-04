from erarigilo.util import *
from .generator import *

@register('prep_until')
def generate_prep_until_manager(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_until',
            word_set = {'until'},
            choice_list = ['by', 'for', 'to', 'in', 'up to', 'when'])

@register('prep_till')
def _prep_till(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_till',
            word_set = {'till'},
            choice_list = ['by', 'for', 'to', 'in', 'up to', 'when'])

