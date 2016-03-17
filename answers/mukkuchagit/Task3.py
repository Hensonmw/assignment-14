#!/usr/bin/env python
# encoding: utf-8
"""
assignment 14.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import glob
import argparse


def sum_all(filename):
    input_file = open(filename)
    sum = 0
    for x in input_file.read().split():
        sum += int(x)
    input_file.close()
    return sum


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_pattern", help="Enter Input File Pattern")
    pattern = parse.parse_args()
    file_list = glob.glob(pattern.input_pattern)

    result = map(sum_all, file_list)
    print('The Sum of all numbers in all the files is: ' + str(sum(result)))


if __name__ == '__main__':
    main()
