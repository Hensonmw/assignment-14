#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task3 to  compute the sum of all integer values across
  all files.
"""

import argparse
import glob
import os
# import shutil


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help='directory to use', type=str)
    args = parser.parse_args()

    return args


def read_files(file1, A):
    """
    read the files and change it to list of string and then convert to int
    """
    with open(file1, "r") as infile:
        file1_read = infile.read()
        file_string = file1_read.split(' ')
        B = (int(i) for i in file_string)
        A.append(B)
        return A


def main():
    args = get_parser()
    A = []
    files = glob.glob(os.path.join(args.directory, "*.txt"))
    for i in files:
        A = read_files(i, A)
    result = map(sum, A)
    print(sum(result))

if __name__ == '__main__':
    main()
