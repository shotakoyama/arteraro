from arteraro.erarigilo.util import *

class ArticleChoiceSamplingCaseFittingTokenWiseMistaker(ChoiceSamplingCaseFittingTokenWiseMistaker):
    def __init__(self):
        super().__init__('art',
                ['', 'a', 'an', 'the',
                    'this', 'that', 'these', 'those'],
                p = [0.2, 0.2, 0.2, 0.3,
                    0.025, 0.025, 0.025, 0.025])

    def cond(self, token):
        return (token.lower in {'a', 'an', 'the'}
                and token.pos == 'DET')


@register('art')
def _art(dct):
    generator = TokenWiseGenerator(ArticleChoiceSamplingCaseFittingTokenWiseMistaker)
    return generator(dct)

