from arteraro.erarigilo.util import *
import random as rd
from lemminflect import getInflection, getAllInflections, getAllInflectionsOOV

def sample_cand(tag_list, source_tag, source):
    tag_list = [tag
            for tag
            in tag_list
            if tag != source_tag]
    tag = rd.choice(tag_list)
    cand_list = getInflection(source, tag)
    cand = rd.choice(cand_list)
    return cand


class InflectionMistaker(Mistaker):
    def cond(self, token):
        return token.tag in self.tag_list

    def __call__(self, token):
        if token.org is not None:
            word = token.org
        else:
            word = token.lemma
        if word != '':
            source_tag = token.tag
            cand = sample_cand(self.tag_list, source_tag, word.lower())
            if word.istitle():
                cand = cand.title()
            token.org = cand
            token = self.add_history(token)
        return token


class AdjectiveInflectionMistaker(InflectionMistaker):
    def __init__(self):
        super().__init__('adj_infl')
        self.tag_list = {'JJ', 'JJR', 'JJS'}


class NounInflectionMistaker(InflectionMistaker):
    def __init__(self):
        super().__init__('noun_infl')
        self.tag_list = {'NN', 'NNS'}


@register('adj_infl')
def _adj_infl(dct):
    generator = TokenWiseGenerator(AdjectiveInflectionMistaker)
    return generator(dct)

@register('noun_infl')
def _noun_infl(dct):
    generator = TokenWiseGenerator(NounInflectionMistaker)
    return generator(dct)

