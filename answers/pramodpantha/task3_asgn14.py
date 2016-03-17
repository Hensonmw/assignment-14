#!/usr/bin/env python
# utf-8

"""
Program for task3 of assignment 14
Created by Pramod Pantha on 15 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


import argparse
import glob
import os


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help='directory to use', type=str)
    args = parser.parse_args()
    return args


def read_files(file1, P):
    with open(file1, "r") as infile:
        file1_read = infile.read()
        file_string = file1_read.split(' ')
        Q = (int(i) for i in file_string)
        P.append(Q)
        return P


def main():
    args = get_parser()
    P = []
    files = glob.glob(os.path.join(args.directory, "*.txt"))
    for i in files:
        P = read_files(i, P)
    result = map(sum, P)
    print(sum(result))

if __name__ == '__main__':
    main()
