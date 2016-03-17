#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 14 Task 2

Using a combination of argparse and glob to read the files in a directory then
using map to compute the sum of all integer values across all files.
'''

import argparse
import os
import glob


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        required=True,
        help="""Include a directory you would like to read files from"""
    )
    return parser.parse_args()


def read_directory(args):
    list_of_files = glob.glob(os.path.join(args.directory, "*"))
    return list_of_files


def sum_ints(list_of_files):
    for a_file in list_of_files:
        with open(a_file, 'r') as f:
            my_str = f.read()
            my_list = my_str.split(' ')
            result = sum(list(map(int, my_list)))
            print(result)
            return result


def main():
    args = get_args()
    list_of_files = read_directory(args)
    sum_ints(list_of_files)


if __name__ == '__main__':
    main()
