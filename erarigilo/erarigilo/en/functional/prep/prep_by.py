from erarigilo.util import *
from .generator import *

@register('prep_by')
def _prep_by(dct):
    return generate_sampling_prep_generator(dct,
            name = 'prep_by',
            word_set = {'by'},
            choice_list = ['', 'in', 'on', 'at', 'for', 'with', 'of', 'from', 'through', 'until', 'till'])

