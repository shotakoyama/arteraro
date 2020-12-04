from erarigilo.util import *
from .generator import *

@register('prep_as')
def _prep_as(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_as',
            word_set = {'as'},
            choice_list = ['by', 'of', 'in', 'on', 'at', 'like'])

