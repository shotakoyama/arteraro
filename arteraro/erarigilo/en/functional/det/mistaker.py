from arteraro.erarigilo.util import *

class TokenWiseMistakerDeterminerConditioned(MistakerWordConditionable):
    def cond(self, token):
        return (self.word_cond(token)
                and token.pos == 'DET')


class DeterminerChoiceSamplingCaseFittingTokenWiseMistaker(TokenWiseMistakerDeterminerConditioned, WordConditionedChoiceSamplingCaseFittingTokenWiseMistaker):
    pass

