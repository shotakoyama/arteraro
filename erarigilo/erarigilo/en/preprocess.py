import sys
import json
import spacy
from erarigilo.en.util.token import EnToken
from erarigilo.en.util.sent import EnSent
from reguligilo.encode import Encoder

def space_normalization(x):
    return ' '.join(x.split())

def convert_token(tok):
    return EnToken(
            index = tok.i,
            cor = tok.text,
            tag = tok.tag_,
            pos = tok.pos_,
            dep = tok.dep_,
            lemma = tok.lemma_,
            norm = tok.norm_,
            lower = tok.lower_,
            ent_type = tok.ent_type_,
            ent_iob = tok.ent_iob_,
            )


class SpacyWrapper:
    def __init__(self):
        self.nlp = spacy.load('en')

    def line_to_doc(self, line):
        line = line.strip()
        line = space_normalization(line)
        doc = self.nlp(line)
        return doc


class ReguligiloWrapper:
    def __init__(self):
        self.encoder = Encoder()

    def convert_token(self, tok):
        text = self.encoder(tok.text)
        return EnToken(
                index = tok.i,
                cor = text,
                tag = tok.tag_,
                pos = tok.pos_,
                dep = tok.dep_,
                lemma = tok.lemma_,
                norm = tok.norm_,
                lower = tok.lower_,
                ent_type = tok.ent_type_,
                ent_iob = tok.ent_iob_,
                )

    def doc_to_sent(self, doc):
        sent = [self.convert_token(token) for token in doc]
        sent = EnSent(sent)
        return sent


def main():
    nlp = SpacyWrapper()
    encoder = ReguligiloWrapper()
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        sent = encoder.doc_to_sent(doc)
        js = json.dumps(sent.encode(), ensure_ascii = False)
        print(js)


def tokenization():
    nlp = SpacyWrapper()
    nlp.nlp.pipeline = nlp.nlp.pipeline[:1]
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        print(' '.join([x.text for x in doc]))

