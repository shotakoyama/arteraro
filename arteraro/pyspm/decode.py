import sys

def main():
    for x in sys.stdin:
        x = x.strip()
        x = ''.join(x.split()).replace('▁', ' ')
        x = x.strip()
        print(x)

