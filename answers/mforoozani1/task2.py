#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task2 to copy only the fastq files to a new directory
"""

import argparse
import glob
import os
import shutil


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputdirectory", help='directory to use', type=str)
    parser.add_argument("--outputdirectory", help='directory to use', type=str)
    args = parser.parse_args()

    return args


def main():
    args = get_parser()
    file1 = glob.glob(os.path.join(args.inputdirectory, "*.fastq"))
    for filename in file1:
        shutil.copy(filename, args.outputdirectory)

if __name__ == '__main__':
    main()
