from erarigilo.util import *
from .generator import *

@register('1sng_subj')
def _1sng_subj(dct):
    return generate_sampling_first_singular_pron_generator(dct,
            name = '1sng_subj',
            word_cond = lambda token : token.cor == 'I' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'attr'},
            choice_list = ['', 'i', 'it', 'me', 'we'])

@register('1sng_nsubj_obj')
def _1sng_nsubj_obj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_nsubj_obj',
            word_cond = lambda token : token.norm == 'me' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'attr'},
            choice_list = ['', 'I', 'my'])

@register('1sng_dobj')
def _1sng_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_dobj',
            word_cond = lambda token : token.norm == 'me' and token.dep == 'dobj',
            choice_list = ['', 'I', 'for me', 'to me', 'on me', 'in me', 'at me', 'of me'],
            p = [0.1, 0.1, 0.3, 0.3, 0.05, 0.05, 0.05, 0.05])

@register('1sng_pobj')
def _1sng_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_pobj',
            word_cond = lambda token : token.norm == 'me' and token.dep == 'pobj',
            choice_list = ['', 'I', 'my'])

@register('1sng_dative')
def _1sng_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_dative',
            word_cond = lambda token : token.norm == 'me' and token.dep == 'dative',
            choice_list = ['', 'I', 'for me', 'to me', 'on me', 'in me', 'at me'],
            p = [0.1, 0.1, 0.3, 0.35, 0.05, 0.05, 0.05])

@register('1sng_poss')
def _1sng_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_poss',
            word_cond = lambda token : token.norm == 'mine',
            choice_list = ['my', 'me', 'ours', 'his', 'hers'])

@register('1sng_poss_det')
def _1sng_poss_det(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_poss_det',
            word_cond = lambda token : token.norm == 'my',
            choice_list = ['', 'I', 'me', 'mine', 'a', 'an', 'the', 'its', 'his', 'her', 'their'])

@register('1sng_reflexive')
def _1sng_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_reflexive',
            word_cond = lambda token : token.norm == 'myself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to myself', 'of myself', 'for myself', 'by myself', 'with myself',
                'myselves', 'to myselves', 'of myselves', 'for myselves', 'by myselves', 'with myselves',
                'me', 'my', 'mine', 'yourself', 'ourselves'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                0.1, 0.02, 0.02, 0.02, 0.02])

@register('1sng_appos_reflexive')
def _1sng_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_appos_reflexive',
            word_cond = lambda token : token.norm == 'myself' and token.dep == 'appos',
            choice_list = ['', 'me', 'myselves', 'my self', 'for myself', 'by myself'])

@register('1sng_pobj_reflexive')
def _1sng_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '1sng_pobj_reflexive',
            word_cond = lambda token : token.norm == 'myself' and token.dep == 'pobj',
            choice_list = ['me', 'my self', 'myselves', 'I'])


