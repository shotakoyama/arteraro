from .util import load_fore_rule
from .checker import Checker

class Encoder:
    def __init__(self, name = 'base', quote = False, rev = False, full = False, rm_zero = False):
        self.rule = load_fore_rule(quote)
        self.checker = Checker(name)
        self.rev = rev
        self.full = full
        self.rm_zero = rm_zero

    def apply_rule(self, char):
        if char in self.rule:
            char = self.rule[char]
        return char

    def regularize(self, chars):
        chars = [self.apply_rule(char) for char in chars]
        chars = ''.join(chars)
        return chars

    def check(self, text):
        if self.full:
            p = True
        else:
            p = self.checker(text) ^ self.rev
        return p

    def __call__(self, text):
        text = text.strip()

        text = self.regularize(text)

        if not self.check(text):
            return None

        text = ' '.join(text.split())

        if self.rm_zero and len(text) == 0:
            return None

        return text

