#! /usr/bin/env python
# encoding UTF-8

'''
Assignment14Task3 biol7800
ZacCarver 03/15/2016
In the directory task3-files there are 10 files, each containing a random
selection of integer values. Using a combination of argparse and glob, read
these files. Then, use map to compute the sum of all integer values across all
files. Your program should contain a main loop and an ifmain statement, and it
should be formatted correctly.
'''

import argparse
import glob
import os
import re


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str,
                        help="provide a path containing files with some nums")
    return parser.parse_args()


def globberdir(directory):
    files = glob.glob(os.path.join(directory, '*.txt'))
    ls = []
    for f in files:
        with open(f, 'r') as a:
            x = a.read()
            x = re.split('\W+', x)
            i = (int(d) for d in x)
            ls.append(i)
    return ls


def main():
    arg = args()
    r = globberdir(arg.directory)
    s = map(sum, r)
    print(sum(s))

if __name__ == '__main__':
    main()
