from erarigilo.util import *

class LowerCaseTokenWiseMistaker(TokenWiseMistaker):
    def __init__(self):
        super().__init__('uncase')

    def word_cond(self, token):
        word = token.word()
        return (not word.islower()) and (not word.isdigit()) and word.isalnum()

    def cond(self, token):
        return token.ent_iob == 'O' and self.word_cond(token)

    def mistake(self, token):
        return token.word().lower()

@register('uncase')
def _uncase(dct):
    generator = TokenWiseGenerator(LowerCaseTokenWiseMistaker)
    return generator(dct)

