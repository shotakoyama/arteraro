import sys
import json

def main():
    for x in sys.stdin:
        x = x.strip()
        x = {'trg': x}
        x = json.dumps(x, ensure_ascii = False)
        print(x)

