from erarigilo.util import *
from .generator import *

@register('prep_under')
def _prep_under(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_under',
            word_set = {'under'},
            choice_list = ['in', 'on', 'by', 'with', 'below', 'through', 'within'])

