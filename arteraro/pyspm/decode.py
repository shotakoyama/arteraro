import sys
from argparse import ArgumentParser

def decode():
    for x in sys.stdin:
        x = x.strip()
        x = ''.join(x.split()).replace('▁', ' ')
        x = x.strip()
        print(x)

def decode_with_removing_unk():
    for x in sys.stdin:
        x = x.strip()
        x = x.split()
        x = [token for token in x if token != '<unk>']
        x = ''.join(x).replace('▁', ' ')
        x = x.strip()
        print(x)

def decode_with_replacing_unk(unk_token):
    for x in sys.stdin:
        x = x.strip()
        x = x.split()
        x = [unk_token if token == '<unk>' else token for token in x]
        x = ''.join(x).replace('▁', ' ')
        x = x.strip()
        print(x)

def main():
    parser = ArgumentParser()
    parser.add_argument('--replace-unk', default=None)
    parser.add_argument('--remove-unk', action = 'store_true')
    args = parser.parse_args()

    if args.remove_unk:
        decode_with_removing_unk()
    elif args.replace_unk:
        decode_with_replacing_unk(args.replace_unk)
    else:
        decode()

