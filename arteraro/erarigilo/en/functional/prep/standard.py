from arteraro.erarigilo.util import *
from .generator import *

@register('standard_prep')
def _standard_prep(dct):
    return generate_sampling_prep_generator(dct,
            name = 'standard_prep',
            word_set = {'of', 'to', 'in', 'for', 'on', 'with', 'at'},
            choice_list = ['', 'of', 'to', 'in', 'for', 'on', 'with', 'by', 'at'])

