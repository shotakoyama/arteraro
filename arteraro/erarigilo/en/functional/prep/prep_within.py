from arteraro.erarigilo.util import *
from .generator import *

@register('prep_within')
def _prep_within(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_within',
            word_set = {'within'},
            choice_list = ['with', 'in', 'of', 'on'])

