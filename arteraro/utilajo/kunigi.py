import sys
from contextlib import ExitStack
from argparse import ArgumentParser

class Parallel:
    def __init__(self, src_file, trg_file):
        self.src_file = src_file
        self.trg_file = trg_file
        self.feed()

    def empty(self):
        return self.index is None

    def top(self):
        return self.index, self.src, self.trg

    def feed(self):
        src = self.src_file.readline()
        trg = self.trg_file.readline()
        if src == '':
            self.index = None
            self.src = None
            self.trg = None
        else:
            index, trg = trg.split('\t')
            self.index = index
            self.src = src.strip()
            self.trg = trg.strip()

class Kunigilo:
    def __init__(self, src_files, trg_files):
        assert len(src_files) == len(trg_files)
        self.corpora = [Parallel(src_file, trg_file) for src_file, trg_file in zip(src_files, trg_files)]

    def check(self):
        return not all(corpus.empty() for corpus in self.corpora)

    def extract_heads(self):
        min_index = min([corpus.index for corpus in self.corpora if not corpus.empty()])
        heads = []
        for corpus in self.corpora:
            if corpus.index == min_index:
                heads.append(corpus)
        return heads

    def feed(self):
        heads = self.extract_heads()
        srcs = [corpus.src for corpus in heads]
        trgs = [corpus.trg for corpus in heads]
        assert len(set(trgs)) == 1
        for corpus in heads:
            corpus.feed()
        line = '\t'.join(trgs[0:1] + srcs)
        return line

def main():
    parser = ArgumentParser()
    parser.add_argument('src')
    parser.add_argument('trg')
    args = parser.parse_args()

    src_list = args.src.split(':')
    trg_list = args.trg.split(':')
    with ExitStack() as stack:
        src_files = [stack.enter_context(open(filename)) for filename in src_list]
        trg_files = [stack.enter_context(open(filename)) for filename in trg_list]
        ilo = Kunigilo(src_files, trg_files)
        while ilo.check():
            line = ilo.feed()
            print(line)

