from pathlib import Path

def load_rule():
    rule = {}
    with open(Path(__file__).parent / 'rule.tsv') as f:
        for line in f:
            src = line[0]
            trg = line[2:-1]
            rule[src] = trg
    return rule

def load_reverse():
    rule = []
    with open(Path(__file__).parent / 'reverse.tsv') as f:
        for line in f:
            src = line[0:-3]
            trg = line[-2:-1]
            rule.append([src, trg])
    rule.sort(key = lambda x : - len(x[0]))
    return rule

