#! /usr/bin/env python
# encoding UTF-8

'''
Assignment14Task1 biol7800
ZacCarver 03/15/2016
There are 2 chapters of Darwin's Origin of Species in this repository within a
directory entitled task1-files. Write a program that uses argparse and glob to
open and read these chapters and some other code to get a list of all words in
each chapter. Then output, to the command line, a pretty-printed list of the
following:
    ~the total count of words in Chapter 1
    ~the count of unique words in Chapter 1
    ~the total count of words in Chapter 2
    ~the count of unique words in Chapter 2
    ~the count of words in Chapter 1 that ARE in Chapter 2
    ~the count of words in Chapter 1 that ARE NOT in Chapter 2
    ~the count of words in Chapter 2 that ARE NOT in Chapter 1
'''

import argparse
from collections import Counter
import glob
import os
import re


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=str,
                        help="provide a path to a couple of files")
    return parser.parse_args()

'''
def clean(f):
    txt = re.sub(r'\W+', ' ', f)
    txt = txt.lower()
    return txt
'''


def ls(f):
    with open(f, 'r') as txt:
        txt = txt.read().lower()
        txt = re.sub(r'\W+', ' ', txt)
        txt = re.sub('[.]', ' ', txt)
        ls = list(txt.split())
        return ls


def uni(f, ls):
    s = set(ls)
    counts = Counter()
    counts.update(s)
    print('{} words are unique to {}'.format(len(counts), f))


def setting(ls):
    s = set(ls)
    return s


def main():
    arg = args()
    files = glob.glob(os.path.join(arg.directory, '*.txt'))
    files = sorted(files)
    f1 = files[0]
    f2 = files[1]
    #txt = clean(f1)
    #txt2 = clean(f2)
    ls1 = ls(f1)
    ls2 = ls(f2)
    uni(f1, ls1)
    uni(f2, ls2)
    s1 = setting(ls1)
    s2 = setting(ls2)
    same = s1.intersection(s2)
    diff = s1.difference(s2)
    diff2 = s2.difference(s1)
    print('words that are shared between both files: {}'.format(len(same)))
    print('words that are unique to file one: {}'.format(len(diff)))
    print('words that are unique to file two: {}'.format(len(diff2)))
    print('total # of words in file1: {}'.format(len(ls1)))
    print('total # of words in file2: {}'.format(len(ls2)))

if __name__ == '__main__':
    main()
