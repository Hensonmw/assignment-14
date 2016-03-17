#!/usr/bin/env python
# encoding: utf-8
"""
assignment 14.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import glob
import argparse
import os
import shutil


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_directory", help="Enter Input Directory")
    parse.add_argument("output_directory", help="Enter Output File Directory")

    dirs = parse.parse_args()
    input_dir = dirs.input_directory
    output_dir = dirs.output_directory
    for filename in glob.glob(os.path.join(input_dir, '*.fastq')):
        shutil.copy(filename, output_dir)


if __name__ == '__main__':
    main()
