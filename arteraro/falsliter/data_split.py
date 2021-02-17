import sys
from argparse import ArgumentParser
import gzip

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('outputs')
    args = parser.parse_args()
    return args

def get_chunk_end_list(data, N):
    data_size = sum(len(sent) for sent in data)
    chunk_size = data_size // N
    chunk_end_list = [chunk_size * (n + 1) - 1 for n in range(N)]
    return chunk_end_list

def split_data_to_chunk(data, N):
    i = 0
    accum = 0
    chunk_list = []
    for chunk_end in get_chunk_end_list(data, N):
        chunk = []
        while accum < chunk_end:
            chunk.append(data[i])
            accum += len(data[i])
            i += 1
        chunk_list.append(chunk)
    return chunk_list

def main():
    args = parse_args()
    data = sys.stdin.readlines()

    output_path_list = args.outputs.split(':')
    N = len(output_path_list)

    for output_path, chunk in zip(output_path_list, split_data_to_chunk(data, N)):
        with gzip.open(output_path, 'wt') as f:
            for x in chunk:
                f.write(x)

