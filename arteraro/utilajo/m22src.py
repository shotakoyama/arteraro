import sys

def m2_to_src():
    for x in sys.stdin:
        x = x.strip()
        if x.startswith('S '):
            print(x[2:])

