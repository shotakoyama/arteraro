import sys
import json
import spacy
from argparse import ArgumentParser
from spacy_langdetect import LanguageDetector
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
    def __init__(self, remove_non_english=False, remove_tagger_and_ner=False):
        self.nlp = spacy.load('en')
        if remove_tagger_and_ner:
            self.nlp.pipeline = self.nlp.pipeline[1:2]
        if remove_non_english:
            self.nlp.add_pipe(LanguageDetector(), name = 'language_detector', last = True)

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
    parser = ArgumentParser()
    parser.add_argument('--remove-non-english', action='store_true')
    args = parser.parse_args()

    nlp = SpacyWrapper(remove_non_english=args.remove_non_english)
    encoder = ReguligiloWrapper()
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        if args.remove_non_english and doc._.language['language'] != 'en':
            continue
        sent = encoder.doc_to_sent(doc)
        if len(sent) > 0:
            js = json.dumps(sent.encode(), ensure_ascii = False)
            print(js)


def tokenization():
    parser = ArgumentParser()
    parser.add_argument('--remove-non-english', action='store_true')
    args = parser.parse_args()

    nlp = SpacyWrapper(remove_non_english=args.remove_non_english, remove_tagger_and_ner=True)
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        if args.remove_non_english and doc._.language['language'] != 'en':
            continue
        if len(doc) > 0:
            print(' '.join([x.text for x in doc]))

