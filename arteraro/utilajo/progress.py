import sys
from tqdm import tqdm

def progress_bar():
    for x in tqdm(sys.stdin):
        print(x, end = '')

def main():
    try:
        progress_bar()
    except BrokenPipeError:
        pass
    except KeyboardInterrupt:
        pass

