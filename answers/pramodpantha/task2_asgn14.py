#!/usr/bin/env python
# utf-8

"""
Program for asignment 14, task2.
Created by Pramod Pantha on 15 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
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
    # http://stackoverflow.com/questions/18262293/python-open-every-file-in-a-folder

if __name__ == '__main__':
    main()
