#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 14 Task 2

A program that uses argparse, glob, and os to copy only the fastq files to a
new directory specified by the user.
'''

import argparse
import string
from collections import Counter
import os
import copy
import glob


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        required=True,
        help="""Include a directory you would like to read files from"""
    )
    parser.add_argument(
        "--output",
        required=True,
        help="""Name a new directory to output files, no path needed. Will
        output to within input directory"""
    )
    return parser.parse_args()


def get_files(args):
    new_files = []
    os.chdir(args.directory)
    fastqlist = glob.glob('*.fastq')
    new_files.extend(copy.deepcopy(fastqlist))
    return new_files


def write_to_output(args, new_files):
    outfiles = []
    os.mkdir(args.output)
    for item in new_files:
        outfiles.append(os.path.join(args.output, item))
    for item in outfiles:
        open(item, 'w')

def main():
    args = get_args()
    new_files = get_files(args)
    write_to_output(args, new_files)

if __name__ == '__main__':
    main()
