from erarigilo.util import *
from .generator import *

@register('prep_against')
def _prep_against(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_against',
            word_set = {'against'},
            choice_list = ['to', 'for', 'of', 'with'])

