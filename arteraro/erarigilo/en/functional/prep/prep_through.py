from arteraro.erarigilo.util import *
from .generator import *

@register('prep_through')
def _prep_through(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_through',
            word_set = {'through'},
            choice_list = ['in', 'over', 'across', 'into', 'of', 'with', 'by', 'throughout', 'thru'])

