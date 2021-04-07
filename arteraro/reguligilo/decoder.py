from .util import load_back_rule

class Decoder:
    def __init__(self):
        self.rule = load_back_rule()

    def __call__(self, text):
        text = text.strip()

        for src, trg in self.rule:
            text = text.replace(src, trg)

        return text

