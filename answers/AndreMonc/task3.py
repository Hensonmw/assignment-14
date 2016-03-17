# !/usr/bin/env python
# encoding: utf-8


"""
My summing-across-files program
Created by Andre Moncrieff on 14 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import argparse
import os
import glob


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_path", required=True,
                        help="Enter '--dir_path', space, and then the" +
                        " path of the directory containing the files of" +
                        "interest.",
                        type=str)
    args = parser.parse_args()
    return args


class Integers:
    def __init__(self, dir_path):
        # set things up
        self.dir_path = dir_path
        self.list_of_filenames = self.list_of_filenames()
        # self.map_answer = self.map_answer()
        self.int_list_of_lists = self.compile_lists()

    def list_of_filenames(self):
        os.chdir(self.dir_path)
        list_of_filenames = glob.glob("*.txt")
        return list_of_filenames

    def compile_lists(self):
        os.chdir(self.dir_path)
        number_list = []
        for filename in self.list_of_filenames:
            opened_file = open(filename, "r")
            for line in opened_file:
                if line != "\n":
                    parsed = line.split(" ")
                    number_list.append(parsed)
        return number_list


def int_parse(nums, list_o_lists):
    start_list = []
    int_list = []
    start_list.extend(list_o_lists[nums])
    # print(type(start_list))
    for item in start_list:
        int_list.append(int(item))
    return sum(int_list)


def main():
    args = parser()
    integer_master = Integers(args.dir_path)
    int_list_of_lists = integer_master.int_list_of_lists
    nums = range(0, 10)
    result = sum(map(int_parse, nums, [int_list_of_lists]*len(nums)))
    print("\nSum of all integer values across all files: ", result, "\n")


if __name__ == '__main__':
    main()
