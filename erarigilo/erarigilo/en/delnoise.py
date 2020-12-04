from erarigilo.util import *

class DeleteReplacingTokenWiseMistaker(ReplacingTokenWiseMistaker):
    def __init__(self):
        super().__init__('del', target = '')
        tokens = [',', '.', '-', '"', "'", ')', '(', ':', '$', '/', ';', '?', '%', '&', '=', '_', '!', '[', ']', '@', '*', '+', '<', '`', '#', '>', '\\', '{', '~', '}', '^']
        tokens += ['the', 'a', 'an']
        tokens += ["'s", "'re"]
        tokens += ['to', 'of', 'in', 'for', 'on', 'with', 'as', 'at', 'by', 'from', 'about', 'than', 'into', 'against', 'under', 'during', 'around']
        tokens += ['up', 'down', 'before', 'after', 'out', 'over', 'like', 'back', 'off', 'away', 'back', 'through', 'just']
        tokens += ['am', 'was', 'are', 'were', 'is', 'be', 'being', 'been']
        tokens += ['have', 'has', 'had']
        tokens += ['do', 'did', 'does']
        tokens += ['and', 'or', 'but', 'because', 'if', 'since', 'while']
        tokens += ['this', 'these', 'that', 'those', 'there']
        tokens += ['it', 'they', 'them']
        tokens += ['which', 'what', 'whose', 'who', 'whom', 'where', 'when', 'how', 'why', 'whether']
        tokens += ['can', 'could', 'may', 'might', 'ought', 'shall', 'should', 'will', 'would', 'dare']
        self.token_set = set(tokens)

    def cond(self, token):
        return token.word().lower() in self.token_set


@register('del')
def _del(dct):
    generator = TokenWiseGenerator(DeleteReplacingTokenWiseMistaker)
    return generator(dct)

