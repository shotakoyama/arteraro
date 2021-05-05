import sys
import json
from contextlib import ExitStack
from argparse import ArgumentParser

class Parallel:
    def __init__(self, lang, indices_file, source_file):
        self.lang = lang
        self.indices_file = indices_file
        self.source_file = source_file
        self.feed()

    def empty(self):
        return self.index is None

    def top(self):
        return self.index, self.source

    def feed(self):
        index = self.indices_file.readline().strip()
        source = self.source_file.readline().strip()
        if index == '': # end of file
            self.index = None
            self.source = None
        else:
            self.index = int(index)
            self.source = source


class Kunigilo:
    def __init__(self, lang_list, indices_files, source_files, target_file):
        self.corpora = [Parallel(lang, indices_file, source_file)
                for lang, indices_file, source_file
                in zip(lang_list, indices_files, source_files)]
        self.target_file = target_file
        self.index = 0

    def check(self):
        return not all(corpus.empty() for corpus in self.corpora)

    def extract_heads(self):
        heads = [corpus
                for corpus
                in self.corpora
                if corpus.index == self.index]
        return heads

    def feed(self):
        target = self.target_file.readline().strip()
        dct = {'trg': target}
        for corpus in self.corpora:
            if corpus.index == self.index:
                dct[corpus.lang] = corpus.source
                corpus.feed()
            else:
                dct[corpus.lang] = None
        self.index += 1
        return dct


def main():
    parser = ArgumentParser()
    parser.add_argument('langs')
    parser.add_argument('indices')
    parser.add_argument('source')
    parser.add_argument('target')
    args = parser.parse_args()

    lang_list = args.langs.split(':')
    indices_list = args.indices.split(':')
    source_list = args.source.split(':')
    target = args.target
    assert len(lang_list) == len(indices_list) == len(source_list)

    with ExitStack() as stack:
        indices_files = [stack.enter_context(open(filename)) for filename in indices_list]
        source_files = [stack.enter_context(open(filename)) for filename in source_list]
        target_file = stack.enter_context(open(target))

        ilo = Kunigilo(lang_list, indices_files, source_files, target_file)
        while ilo.check():
            x = ilo.feed()
            x = json.dumps(x, ensure_ascii = False)
            print(x)

