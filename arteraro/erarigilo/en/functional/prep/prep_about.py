from arteraro.erarigilo.util import *
from .generator import *

@register('prep_about')
def _prep_about(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_about',
            word_set = {'about'},
            choice_list = ['', 'in', 'on', 'of', 'to', 'at'])

