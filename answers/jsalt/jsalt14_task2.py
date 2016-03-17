#! usr/bin/env python
# encoding: utf-8

"""
Assignment 14
Task 2 Program: fastq files
Jessie Salter
14 March 2016
"""

import argparse
import glob
import os
from shutil import copyfile


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the paths of the input and output files.'''
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the path to the directory you want to work from.",
        type=str
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Enter the path to the output directory you want to create.",
        type=str
    )
    return parser.parse_args()


def new_dir(input_file, output):
    '''Copies the contents of the input files to a new output destination.'''
    base = os.path.basename(input_file)
    # This creates the new path including file name and ext for each file:
    newpath = os.path.join(output, base)
    copyfile(input_file, newpath)


def main():
    args = parser()
    if args.input[-1] != '/':
        path_input = args.input + '/'
    else:
        path_input = args.input
    # This creates the new directory with the input path:
    if os.path.isdir(args.output) is True:
        print('Output directory already exists; please re-run with new path.')
    else:
        os.makedirs(args.output)
    # Found this on stack overflow:
    # http://stackoverflow.com/questions/18262293/python-open-every-file-in-a-folder
        for filename in glob.glob(os.path.join(path_input, '*.fastq')):
            new_dir(filename, args.output)

if __name__ == '__main__':
    main()
