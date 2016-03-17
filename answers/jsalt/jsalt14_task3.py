#! usr/bin/env python
# encoding: utf-8

"""
Assignment 14
Task 3 Program: Using `map` to sum across files
Jessie Salter
14 March 2016
"""

import argparse
import glob
import re
import os


def parser():
    '''Takes user input'''
    parser = argparse.ArgumentParser(
        description='''Gets the paths of the input file.'''
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the path to the directory you want to work from.",
        type=str
    )
    return parser.parse_args()


def all_files(input_file, num_list):
    '''Reads the input file and returns a list of all the integers'''
    with open(input_file, 'r') as doc:
        read = doc.read()
        num_strings = re.split('\W+', read)
        num_int = [int(num) for num in num_strings]
        num_list.append(num_int)
        return num_list


def main():
    args = parser()
    num_list = []
    # This adds all the integers across all files to a single list:
    for filename in glob.glob(os.path.join(args.input, '*.txt')):
        num_list = all_files(filename, num_list)
    # This computes the sum for each file:
    results = map(sum, num_list)
    # This computes and prints the sum across all files:
    print(sum(results))


if __name__ == '__main__':
    main()
