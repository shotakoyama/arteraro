from erarigilo.util import *
from .generator import *

@register('3sng_fem_subj')
def _3sng_fem_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_subj',
            word_cond = lambda token : token.norm == 'she' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['her', 'hers', 'they', 'them', 'their', 'he'])

@register('3sng_fem_pobj')
def _3sng_fem_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_pobj',
            word_cond = lambda token : token.norm == 'her' and token.dep == 'pobj',
            choice_list = ['she', 'hers', 'their', 'them', 'herself', 'him'])

@register('3sng_fem_dobj')
def _3sng_fem_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_dobj',
            word_cond = lambda token : token.norm == 'her' and token.dep == 'dobj',
            choice_list = ['', 'she', 'him', 'for her', 'to her', 'on her', 'in her', 'at her', 'of her'],
            p = [0.1, 0.05, 0.05, 0.3, 0.3, 0.05, 0.05, 0.05, 0.05])

@register('3sng_fem_nsubj_obj')
def _3sng_fem_nsubj_obj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_nsubj_obj',
            word_cond = lambda token : token.norm == 'her' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['', 'she', 'hers', 'them', 'him'])

@register('3sng_fem_dative')
def _3sng_fem_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_dative',
            word_cond = lambda token : token.norm == 'her' and token.dep == 'dative',
            choice_list = ['', 'she', 'him', 'for her', 'to her', 'on her', 'in her', 'at her'],
            p = [0.1, 0.05, 0.05, 0.3, 0.35, 0.05, 0.05, 0.05])

@register('3sng_fem_poss')
def _3sng_fem_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_poss',
            word_cond = lambda token : token.norm == 'hers',
            choice_list = ['', 'she', 'her', 'theirs', 'his', 'they', 'yours'])

@register('3sng_fem_poss_det')
def _3sng_fem_poss_det(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_poss_det',
            word_cond = lambda token : token.norm == 'her' and token.dep == 'poss',
            choice_list = ['', 'she', 'hers', 'their', 'his', 'a', 'an', 'the', 'its'])

@register('3sng_fem_reflexive')
def _3sng_fem_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_reflexive',
            word_cond = lambda token : token.norm == 'herself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to herself', 'of herself', 'for herself', 'by herself', 'with herself',
                'herselves', 'to herselves', 'of herselves', 'for herselves', 'by herselves', 'with herselves',
                'themself', 'to themself', 'of themself', 'for themself', 'by themself', 'with themself',
                'she', 'her', 'hers', 'himself'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.045, 0.045, 0.045, 0.045])

@register('3sng_fem_appos_reflexive')
def _3sng_fem_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_appos_reflexive',
            word_cond = lambda token : token.norm == 'herself' and token.dep == 'appos',
            choice_list = ['', 'her', 'themself', 'her self', 'for herself', 'by herself', 'himself'])

@register('3sng_fem_pobj_reflexive')
def _3sng_fem_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_fem_pobj_reflexive',
            word_cond = lambda token : token.norm == 'herself' and token.dep == 'pobj',
            choice_list = ['her', 'her self', 'themself', 'she', 'himself'])

