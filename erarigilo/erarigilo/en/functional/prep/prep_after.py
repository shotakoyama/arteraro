from erarigilo.util import *
from .generator import *

@register('prep_after')
def _prep_after(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_after',
            word_set = {'after'},
            choice_list = ['for', 'by', 'over', 'from', 'when'])

