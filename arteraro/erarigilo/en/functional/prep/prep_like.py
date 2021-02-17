from arteraro.erarigilo.util import *
from .generator import *

@register('prep_like')
def _prep_like(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_like',
            word_set = {'like'},
            choice_list = ['as', 'that', 'than'],
            p = [0.8, 0.1, 0.1])

