from erarigilo.util import *

class MistakerPronConditioned(MistakerWordConditionable):
    def cond(self, token):
        return (self.word_cond(token)
                and (not token.word().isupper()
                    or token.word() == 'I')
                and token.lemma == '-PRON-')


class TokenWiseMistakerFirstSingularPronCaseFitted(TokenWiseMistakerCaseFitted):
    def preprocess(self, token, cand):
        word = token.word()
        if word.istitle() and (word != 'I'):
            cand = cand.title()
        return cand


class FirstSingularPronCaseFittingTokenWiseMistaker(TokenWiseMistakerFirstSingularPronCaseFitted, TokenWiseMistaker):
    pass


class WordConditionedChoiceSamplingFirstSingularPronCaseFittingTokenWiseMistaker(MistakerWordConditionedChoiceSamplable, FirstSingularPronCaseFittingTokenWiseMistaker):
    pass


class PronChoiceSamplingCaseFittingTokenWiseMistaker(MistakerPronConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass


class FirstSingularPronChoiceSamplingCaseFittingTokenWiseMistaker(MistakerPronConditioned, WordConditionedChoiceSamplingFirstSingularPronCaseFittingTokenWiseMistaker):
    pass

