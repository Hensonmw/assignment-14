#!/usr/bin/env python
# utf-8

"""
BIOL 7800 Assignment 14, Task 2
Austen T. Webber
2016_3_15
"""


import argparse
import glob
import os
import shutil


def get_args(parser):
    parser.add_argument("--input",
        required=True,
        help="--input Directory of input files ",
        type=str)

    parser.add_argument("--output",
        required=True,
        help="--output New directory for output files",
        type=str)
    return parser.parse_args()


def main():
    path_name = argparse.ArgumentParser()
    get_args(path_name)
    path_args = path_name.parse_args()
    fastq_files = glob.glob(os.path.join(path_args.input, "*.fastq"))
    os.mkdir(path_args.output)
    for filename in fastq_files:
        shutil.copy(filename, path_args.output)


if __name__ == '__main__':
    main()

#https://docs.python.org/2/library/shutil.html
