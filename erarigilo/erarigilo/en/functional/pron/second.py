from erarigilo.util import *
from .generator import *

@register('2nd_subj')
def _2nd_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_subj',
            word_cond = lambda token : token.norm == 'you' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['u', 'yo', 'your', 'yours', 'me', 'they'])

@register('2nd_pobj')
def _2nd_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_pobj',
            word_cond = lambda token : token.norm == 'you' and token.dep == 'pobj',
            choice_list = ['u', 'yo', 'your', 'yours', 'yourself', 'yourselves'])

@register('2nd_dobj')
def _2nd_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_dobj',
            word_cond = lambda token : token.norm == 'you' and token.dep == 'dobj',
            choice_list = ['', 'u', 'yo', 'for you', 'to you', 'on you', 'in you', 'at you', 'of you'],
            p = [0.1, 0.05, 0.05, 0.3, 0.3, 0.05, 0.05, 0.05, 0.05])

@register('2nd_dative')
def _2nd_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_dative',
            word_cond = lambda token : token.norm == 'you' and token.dep == 'dative',
            choice_list = ['', 'u', 'yo', 'for you', 'to you', 'on you', 'in you', 'at you'],
            p = [0.1, 0.05, 0.05, 0.3, 0.35, 0.05, 0.05, 0.05])

@register('2nd_poss')
def _2nd_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_poss',
            word_cond = lambda token : token.norm == 'yours',
            choice_list = ['you', 'your', 'theirs', 'mine', 'ours', 'theirs'])

@register('2nd_poss_det')
def _2nd_poss_det(dct):
    return generate_sampling_pron_generator(dct,
            name = '2nd_poss_det',
            word_cond = lambda token : token.norm == 'your',
            choice_list = ['', 'you', 'yours', 'their', 'a', 'an', 'the', 'its', 'they'])

@register('2sng_reflexive')
def _2sng_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2sng_reflexive',
            word_cond = lambda token : token.norm == 'yourself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to yourself', 'of yourself', 'for yourself', 'by yourself', 'with yourself',
                'yourselves', 'to yourselves', 'of yourselves', 'for yourselves', 'by yourselves', 'with yourselves',
                'you', 'your', 'yours', 'themself', 'myself'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                0.1, 0.02, 0.02, 0.02, 0.02])

@register('2sng_appos_reflexive')
def _2sng_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2sng_appos_reflexive',
            word_cond = lambda token : token.norm == 'yourself' and token.dep == 'appos',
            choice_list = ['', 'you', 'yourselves', 'your self', 'for yourself', 'by yourself'])

@register('2sng_pobj_reflexive')
def _2sng_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2sng_pobj_reflexive',
            word_cond = lambda token : token.norm == 'yourself' and token.dep == 'pobj',
            choice_list = ['you', 'your self', 'yourselves', 'your'])

@register('2plu_reflexive')
def _2plu_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2plu_reflexive',
            word_cond = lambda token : token.norm == 'yourselves' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to yourselves', 'of yourselves', 'for yourselves', 'by yourselves', 'with yourselves',
                'yourself', 'to yourself', 'of yourself', 'for yourself', 'by yourself', 'with yourself',
                'you', 'your', 'yours', 'themselves', 'ourselves'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.02, 0.02, 0.02, 0.02, 0.02, 0.02,
                0.1, 0.02, 0.02, 0.02, 0.02])

@register('2plu_appos_reflexive')
def _2plu_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2plu_appos_reflexive',
            word_cond = lambda token : token.norm == 'yourselves' and token.dep == 'appos',
            choice_list = ['', 'you', 'yourself', 'your selves', 'for yourselves', 'by yourselves'])

@register('2plu_pobj_reflexive')
def _2plu_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '2plu_pobj_reflexive',
            word_cond = lambda token : token.norm == 'yourselves' and token.dep == 'pobj',
            choice_list = ['you', 'your self', 'myselves', 'your'])

