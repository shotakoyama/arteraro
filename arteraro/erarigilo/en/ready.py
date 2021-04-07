import sys
import json
import spacy
from argparse import ArgumentParser
from .util.token import EnToken
from .util.sent import EnSent
from arteraro.reguligilo.encoder import Encoder

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
            ent_iob = tok.ent_iob_)


class SpacyWrapper:
    def __init__(self, remove_tagger_and_ner=False):
        self.nlp = spacy.load('en')
        if remove_tagger_and_ner:
            self.nlp.pipeline = self.nlp.pipeline[1:2]

    def line_to_doc(self, line):
        line = line.strip()
        line = space_normalization(line)
        doc = self.nlp(line)
        return doc


class ReguligiloWrapper:
    def __init__(self, quote):
        self.encoder = Encoder(quote=quote)

    def convert_token(self, tok):
        text = self.encoder.regularize(tok.text)
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


def en_ready(quote=False):
    nlp = SpacyWrapper()
    encoder = ReguligiloWrapper(quote)

    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        sent = encoder.doc_to_sent(doc)
        if len(sent) > 0:
            js = json.dumps(sent.encode(), ensure_ascii = False)
            print(js)

