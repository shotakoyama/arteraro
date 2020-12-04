from erarigilo.util import *
from .generator import *

@register('agent_by')
def _agent_by(dct):
    return generate_sampling_agent_generator(dct,
            name = 'agent_by',
            word_set = {'by'},
            choice_list = ['', 'of', 'from', 'with', 'on'])

@register('agent_between')
def _agent_between(dct):
    return generate_sampling_agent_generator(dct,
            name = 'agent_between',
            word_set = {'between'},
            choice_list = ['', 'by', 'in', 'on', 'at', 'from', 'with', 'about', 'among', 'amongst', 'amid', 'amidst'])

