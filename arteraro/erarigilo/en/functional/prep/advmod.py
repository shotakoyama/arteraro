from arteraro.erarigilo.util import *
from .generator import *

@register('prep_advmod')
def _prep_advmod(dct):
    return generate_replacing_advmod_generator(dct,
            name = 'prep_advmod',
            source_set = {'at', 'as'},
            target = '')

