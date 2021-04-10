import sys

def allocate_indices():
    for i, line in enumerate(sys.stdin):
        line = line.strip()
        line = '{}\t{}'.format(i, line)
        print(line)

def main():
    try:
        allocate_indices()
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass

