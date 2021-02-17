from arteraro.erarigilo.util import *
from .generator import *

@register('prep_behind')
def _prep_behind(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_behind',
            word_set = {'behind'},
            choice_list = ['after', 'from', 'of', 'out'])

