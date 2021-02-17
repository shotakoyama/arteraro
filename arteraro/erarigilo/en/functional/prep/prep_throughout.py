from arteraro.erarigilo.util import *
from .generator import *

@register('prep_throughout')
def _prep_throughout(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_throughout',
            word_set = {'throughout'},
            choice_list = ['in', 'over', 'across', 'into', 'of', 'with', 'by', 'through'])

