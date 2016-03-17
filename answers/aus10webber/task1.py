#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 14, Task 1
Austen T. Webber
2016_3_15
"""


import argparse
import glob
import os
import re
from collections import Counter

def get_args(parserr):
    parserr.add_argument("--input",
        required=True,
        help="--input Path to directory containing your files",
        type=str)


def darwinchapter1(string):
    list = re.findall(
                "[a-zA-Z]+[-][a-zA-Z]+|[a-zA-z]+['][a-zA-Z]+|[a-zA-Z]+",
                string)
    my_dict = [str.lower(word) for word in list]
    numbers = Counter(my_dict)
    return numbers


def darwinchapter1unique(string):
    uniques = set(string)
    return uniques


def darwinchapter1count(string):
    counters = len(string.split())
    return counters


def main():
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    os.chdir(path_args.input)
    my_files = glob.glob('*.txt')
    with open(my_files[0], 'r') as chapter1:
        readch1 = chapter1.read()
        cleanch1 = darwinchapter1(readch1)
        totalch1 = darwinchapter1count(readch1)
        uniquech1 = darwinchapter1unique(cleanch1)
    print('\r\nTotal count of words in Chapter 1\r\n')
    print(totalch1)
    print('\r\nCount of unique words in Chapter 1\r\n')
    print(len(uniquech1))
    with open(my_files[1], 'r') as chapter2:
        readch2 = chapter2.read()
        cleanch2 = darwinchapter1(readch2)
        totalch2 = darwinchapter1count(readch2)
        uniquech2 = darwinchapter1unique(cleanch2)
    print('\r\nTotal count of words in Chapter 2\r\n')
    print(totalch2)
    print('\r\nCount of unique words in Chapter 2\r\n')
    print(len(uniquech2))
    shared = set(cleanch1).intersection(set(cleanch2))
    print('\r\nCount of words in Chapter 1 that ARE in Chapter 2\r\n')
    print(len(shared))
    print('\r\nCount of words in Chapter 1 that ARE NOT in Chapter 2\r\n')
    onlyinch1 = set(cleanch1).difference(set(cleanch2))
    print(len(onlyinch1))
    print('\r\nCount of words in Chapter 2 that ARE NOT in Chapter 1\r\n')
    onlyinch2 = set(cleanch2).difference(set(cleanch1))
    print(len(onlyinch2))


if __name__ == '__main__':
    main()

#https://docs.python.org/2/library/glob.html
#http://www.tutorialspoint.com/python/os_chdir.htm
