from erarigilo.util import *
from .generator import *

@register('prep_from')
def _prep_from(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_from',
            word_set = {'from'},
            choice_list = ['', 'in', 'at', 'of', 'with', 'about', 'since'])

