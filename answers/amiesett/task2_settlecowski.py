#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 14 Task 2

Amie Settlecowski
16 Mar. 2016

Copy set of files from user-specified input directory to user-specified output
directory.
python task2_settlecowski.py --i \path\to\directory\of\input_files\
--o \path\to\directory\for\output_files\
"""


import argparse
import os
import glob


def get_args(parserr):
    '''
    Requires --i flag for user to indicate path to directory with input files
    requires --o flag for user to indicate path to directory for output files
    '''
    parserr.add_argument("--i",
        required=True,
        help="Path to directory with input files",
        type=str)

    parserr.add_argument("--o",
        required=True,
        help="Path to directory for output files",
        type=str)


def copy_file(f, d):
    ''' Creates copy of file, f in directory, d '''
    path = os.path.abspath(f)
    new_path = os.path.join(d, f)
    with open(path, 'r') as x:
        contents = x.read()
    with open(new_path, 'w') as new_f:
        new_f.write(contents)


def main():
    # creater Parser object with arguments for path to appropriate directory
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    # change directory to input directory
    os.chdir(path_args.i)
    # Collect all text files and create WordCount object for each
    files = glob.glob('*.fastq')

    # create output directory
    os.mkdir(path_args.o)
    for f in files:
        copy_file(f, path_args.o)

if __name__ == '__main__':
    main()
