from erarigilo.util import *

class TitleCaseTokenWiseMistaker(TokenWiseMistaker):
    def __init__(self):
        super().__init__('title')

    def cond(self, token):
        word = token.word()
        return word.islower() and (not word.isdigit()) and word.isalnum()

    def mistake(self, token):
        return token.word().title()


@register('title')
def _title(dct):
    generator = TokenWiseGenerator(TitleCaseTokenWiseMistaker)
    return generator(dct)

