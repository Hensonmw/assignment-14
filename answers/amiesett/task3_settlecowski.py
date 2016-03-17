#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 14 Task 3

Amie Settlecowski
16 Mar. 2016

Compute sum of all integer values across directory of files
python task3_settlecowski.py --dir path\to\directory\with\input_files\
"""


import argparse
import os
import glob


def get_args(parserr):
    '''Requires --dir flag for user to indicate path to input directoy'''
    parserr.add_argument("--dir",
        required=True,
        help="Path to directory with input files",
        type=str)


def construct_list(f):
    ''' Creates copy of file, f in directory, d '''
    path = os.path.abspath(f)
    with open(path, 'r') as x:
        contents = x.read().split(' ')
        return contents


def main():
    # creater Parser object with arguments for path to appropriate directory
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    # change directory to input directory
    os.chdir(path_args.dir)

    # Collect all text files in list
    files = glob.glob('*.txt')

    # loop through files to create master list of all integers
    ints_list = []
    for f in files:
        temp_list = construct_list(f)
        ints_list += (n for n in temp_list)

    # use map() to convert list of strings to integers
    real_ints = list(map(int, ints_list))

    # sum all integers
    summ = sum(real_ints)
    print(summ)
if __name__ == '__main__':
    main()
