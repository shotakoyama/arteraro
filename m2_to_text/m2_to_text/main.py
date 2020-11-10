import sys
from argparse import ArgumentParser

def m2_to_src():
    for x in sys.stdin:
        x = x.strip()
        if x.startswith('S '):
            print(x[2:])

class Edit:
    def __init__(self, line):
        line = line.split('|||')
        self.error_type = line[1]
        self.coder = int(line[-1])
        span = line[0].split()[1:]
        self.start = int(span[0])
        self.end = int(span[1])
        self.cor = line[2].split()

def edit_src(sent, coder):
    offset = 0
    trg = sent.src.copy()
    for edit in sent.edits:
        if edit.error_type not in {'noop', 'UNK', 'Um'} and edit.coder == coder:
            trg[edit.start + offset : edit.end + offset] = edit.cor
            offset += len(edit.cor) - (edit.end - edit.start)
    return trg

class SentencePair:
    def __init__(self, sent, coder = 0):
        sent = sent.split('\n')
        self.src = sent[0].split()[1:]
        self.edits = [Edit(edit) for edit in sent[1:]]
        self.trg = edit_src(self, coder)

def read_m2(f, coder):
    m2 = f.read().strip().split('\n\n')
    m2 = [SentencePair(sent, coder) for sent in m2]
    return m2

def m2_to_trg():
    parser = ArgumentParser()
    parser.add_argument('--coder', type=int, default=0)
    args = parser.parse_args()

    m2 = read_m2(sys.stdin, args.coder)
    for sent in m2:
        print(' '.join(sent.trg))

def remove_identical():
    parser = ArgumentParser()
    parser.add_argument('source_input_path')
    parser.add_argument('target_input_path')
    parser.add_argument('source_output_path')
    parser.add_argument('target_output_path')
    args = parser.parse_args()

    with open(args.source_input_path) as src_in, open(args.target_input_path) as trg_in, open(args.source_output_path, 'w') as src_out, open(args.target_output_path, 'w') as trg_out:
        for src, trg in zip(src_in, trg_in):
            if src != trg:
                print(src.strip(), file = src_out)
                print(trg.strip(), file = trg_out)

