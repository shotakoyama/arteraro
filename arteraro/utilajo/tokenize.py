import sys
import spacy

def space_normalization(x):
    return ' '.join(x.split())

class SpacyWrapper:
    def __init__(self, lang, remove_tagger_and_ner=False):
        self.nlp = spacy.load(lang)
        if remove_tagger_and_ner:
            self.nlp.pipeline = self.nlp.pipeline[1:2]

    def line_to_doc(self, line):
        line = line.strip()
        line = space_normalization(line)
        doc = self.nlp(line)
        return doc

def tokenize(lang):
    nlp = SpacyWrapper(lang, remove_tagger_and_ner=True)
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        print(' '.join([x.text for x in doc]))

def en():
    tokenize('en')

def de():
    tokenize('de')

def fr():
    tokenize('fr')

