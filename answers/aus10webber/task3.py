#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 14, Task 3
Austen T. Webber
2016_3_15
"""


import os
import argparse
import glob


def vol_args(parser):
    parser.add_argument("--input",
        required=True,
        help="--input Directory containing files",
        type=str)


def list_maker(f):
    path = os.path.abspath(f)
    with open(path, 'r') as x:
        contents = x.read().split(' ')
        return contents


def main():
    path_name = argparse.ArgumentParser()
    vol_args(path_name)
    path_args = path_name.parse_args()
    os.chdir(path_args.input)
    files = glob.glob('*.txt')
    ints_list = []
    for f in files:
        temp_list = list_maker(f)
        ints_list += (n for n in temp_list)
    real_ints = list(map(int, ints_list))
    summ = sum(real_ints)
    print(summ)


if __name__ == '__main__':
    main()

#https://docs.python.org/2/howto/argparse.html
