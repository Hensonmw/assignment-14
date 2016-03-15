#!/usr/bin/env python
# utf-8

"""
Assignment 14, Task 3
Jon Nations on 12 March 2016
Subir Shakya and A.J. Turner were critical in making this happen!!!
"""


import argparse
import fileinput
import glob
import os


def file_in():
    """gets input directory containint text files"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, type=str, help="give input directory where all files are stored")
    """parser.add_argument('-t', '--temp', required=True, type=str, help="give temp directory where concatenated values from all files will be stored")
    # parser.add_argument('--output', required=True, help='give output file')"""
    return parser.parse_args()


"""def concatenate(args, my_files):
    temp = []
    for file in my_files:
        with open(file, 'r') as files:
            concat = files.read()
            temp.extend(concat.split(" "))
            files.close()
        return temp"""

"""def summate():
    summed = map(x, temp)
    print(sum(list(summed)))"""


def makeint(numbers):
    return int(numbers)


def main():
    file_in()
    args = file_in()
    my_files = glob.glob(os.path.join(args.directory, "*.txt"))
    temp = []
    for file in my_files:
        with open(file, 'r') as files:
            concat = files.read()
            temp.extend(concat.split(" "))
            files.close()
    summed = map(makeint, temp)
    print(sum(list(summed)))


if __name__ == '__main__':
    main()
