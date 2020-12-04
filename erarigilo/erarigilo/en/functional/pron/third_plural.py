from erarigilo.util import *
from .generator import *

@register('3plu_subj')
def _3plu_subj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_subj',
            word_cond = lambda token : token.norm == 'they' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['them', 'their', 'he', 'him', 'she', 'her', 'themself', 'themselves'])

@register('3plu_pobj')
def _3plu_pobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_pobj',
            word_cond = lambda token : token.norm == 'them' and token.dep == 'pobj',
            choice_list = ['they', 'their', 'him', 'her'])

@register('3plu_dobj')
def _3plu_dobj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_dobj',
            word_cond = lambda token : token.norm == 'them' and token.dep == 'dobj',
            choice_list = ['',
                'they', 'her', 'him',
                'for them', 'to them',
                'on them', 'in them', 'at them', 'of them'],
            p = [0.05, 0.05, 0.05, 0.05,
                0.2, 0.2,
                0.1, 0.1, 0.1, 0.1])

@register('3plu_nsubj_obj')
def _3plu_nsubj_obj(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_nsubj_obj',
            word_cond = lambda token : token.norm == 'them' and token.dep in {'nsubj', 'nsubjpass', 'conj', 'appos', 'nmod', 'compound', 'attr'},
            choice_list = ['', 'they', 'their', 'him', 'her'])

@register('3plu_dative')
def _3plu_dative(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_dative',
            word_cond = lambda token : token.norm == 'them' and token.dep == 'dative',
            choice_list = ['',
                'they', 'him', 'her',
                'for them', 'to them', 'on them', 'in them', 'at them'],
            p = [0.05, 0.05, 0.05, 0.05,
                0.3, 0.35, 0.05, 0.05, 0.05])

@register('3plu_poss')
def _3plu_poss(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_poss',
            word_cond = lambda token : token.norm == 'theirs',
            choice_list = ['', 'they', 'them', 'their', 'its', 'his', 'hers'])

@register('3plu_poss_det')
def _3plu_poss_det(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_poss_det',
            word_cond = lambda token : token.norm == 'their',
            choice_list = ['', 'they', 'them', 'theirs', 'a', 'an', 'the', 'its', 'his', 'her'])

@register('3sng_neut_reflexive')
def _3sng_neut_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_neut_reflexive',
            word_cond = lambda token : token.norm == 'themself' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to themself', 'of themself', 'for themself', 'by themself', 'with themself',
                'themselves', 'to themselves', 'of themselves', 'for themselves', 'by themselves', 'with themselves',
                'himself', 'to himself', 'of himself', 'for himself', 'by himself', 'with himself',
                'herself', 'to herself', 'of herself', 'for herself', 'by herself', 'with herself',
                'she', 'her', 'hers',
                'he', 'him', 'his'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.03, 0.03, 0.03, 0.03, 0.03, 0.03])

@register('3sng_neut_appos_reflexive')
def _3sng_neut_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_neut_appos_reflexive',
            word_cond = lambda token : token.norm == 'themself' and token.dep == 'appos',
            choice_list = ['', 'they', 'them', 'themselves', 'them self', 'for themself', 'by themself', 'by himself', 'herself', 'himself'])

@register('3sng_neut_pobj_reflexive')
def _3sng_neut_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3sng_neut_pobj_reflexive',
            word_cond = lambda token : token.norm == 'themself' and token.dep == 'pobj',
            choice_list = ['them', 'them self', 'herself', 'himself'])

@register('3plu_reflexive')
def _3plu_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_reflexive',
            word_cond = lambda token : token.norm == 'themselves' and token.dep in {'dobj', 'conj', 'nsubj', 'nsubjpass', 'npadvmod', 'dative', 'attr'},
            choice_list = ['',
                'to themselves', 'of themselves', 'for themselves', 'by themselves', 'with themselves',
                'themself', 'to themself', 'of themself', 'for themself', 'by themself', 'with themself',
                'himself', 'to himself', 'of himself', 'for himself', 'by himself', 'with himself',
                'herself', 'to herself', 'of herself', 'for herself', 'by herself', 'with herself',
                'they', 'them', 'their'],
            p = [0.2, 0.1, 0.1, 0.1, 0.1, 0.1,
                0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.005, 0.005, 0.005, 0.005, 0.005, 0.005,
                0.06, 0.06, 0.06])

@register('3plu_appos_reflexive')
def _3plu_appos_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_appos_reflexive',
            word_cond = lambda token : token.norm == 'themselves' and token.dep == 'appos',
            choice_list = ['', 'they', 'them', 'themself', 'them selves', 'for themselves', 'by themselves', 'by himselves', 'herself', 'himself'])

@register('3plu_pobj_reflexive')
def _3plu_pobj_reflexive(dct):
    return generate_sampling_pron_generator(dct,
            name = '3plu_pobj_reflexive',
            word_cond = lambda token : token.norm == 'themselves' and token.dep == 'pobj',
            choice_list = ['them', 'them selves', 'herself', 'himself'])

