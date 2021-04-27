from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('spm')
    parser.add_argument('fsq')
    args = parser.parse_args()

    with open(args.spm) as f:
        spm_tokens = [line.split('\t')[0] for line in f]

    with open(args.fsq) as f:
        fsq_tokens = [line.split()[0] for line in f]

    print(set(spm_tokens) - set(fsq_tokens))
    print(set(fsq_tokens) - set(spm_tokens))

