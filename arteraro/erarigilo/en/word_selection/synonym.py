import random as rd
from arteraro.erarigilo.util import *
from nltk.corpus import wordnet as wn

def synsets(word):
    return {synonym
            for synset in wn.synsets(word)
            for synonym in synset.lemma_names()
            if synonym.isalpha()} - {word}


class SynonymMistaker(Mistaker):
    def __init__(self):
        super().__init__('synonym')

    def cond(self, token):
        return token.tag in {'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'RB', 'RBR', 'RBS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'}

    def __call__(self, token):
        word = token.word()
        synonyms = synsets(word)

        if len(synonyms) > 0:
            cand = rd.choice(list(synonyms))
            if word.istitle():
                cand = cand.title()
            token.org = cand
            token = self.add_history(token)
        return token


@register('synonym')
def _synonym(dct):
    generator = TokenWiseGenerator(SynonymMistaker)
    return generator(dct)

