from arteraro.erarigilo.util import *
from .generator import *

# The most frequent usage of ``since'' as preposition is ``origin of time''.
# So, it is enough to simply replace ``since'' to ``from''.
@register('prep_since')
def _prep_since(dct):
    return generate_replacing_prep_generator(dct,
            name = 'prep_since',
            source_set = {'since'},
            target = 'from')

