from pathlib import Path

def load_fore_rule(quote):
    rule = {}
    if quote:
        filename = 'rule/quote_fore.tsv'
    else:
        filename = 'rule/fore.tsv'
    with open(Path(__file__).parent / filename) as f:
        for line in f:
            src = line[0]
            trg = line[2:-1]
            rule[src] = trg
    return rule

def load_back_rule():
    rule = []
    with open(Path(__file__).parent / 'rule' / 'back.tsv') as f:
        for line in f:
            src = line[0:-3]
            trg = line[-2:-1]
            rule.append([src, trg])
    rule.sort(key = lambda x : - len(x[0]))
    return rule

