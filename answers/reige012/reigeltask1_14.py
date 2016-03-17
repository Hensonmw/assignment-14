#!/usr/bin/env python
# encoding: utf-8

"""
This program counts the words in two chapters of Darwin's work. It then finds
which words are in common and not in common between the chapters.

Edited by Alicia Reigel. 12 March 2016.
Copyright Alicia Reigel. Louisiana State University. 12 March 2016. All
rights reserved.

"""


import glob
import os
import argparse
import re


def parser_directorypath():
    """Collects the path of the directory where your files are"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the directory of interest"""
        )
    parser.add_argument(
            '--directorypath',
            required=True,
            type=str,
            help='Enter the path to the directory of interest.'
        )
    return parser.parse_args()


def total_words(filename):
    """counts the total words in the given file"""
    with open(filename, 'r') as the_string:
        all_of_it = the_string.read()
        total_words = len(all_of_it.split(' '))
        return total_words


def make_sets(filename):
    """cleans up the string and creates sets of unique words from the text"""
    with open(filename, 'r') as input_data:
        a_string = input_data.read()
        clean_string = a_string.replace('  ', ' ').casefold()
        # substitutes spaces and lowers case
        the_new_list = re.split('\W+', clean_string)
        # splits on spaces to make a list of words
        the_set = set(the_new_list)
        return the_set


def count_unique_words(the_set):
    """counts the number of unique words in a set"""
    how_many = len(the_set)
    return how_many


def common_set(set1, set2):
    """counts the number of words that two sets have in common"""
    common_set = set1.intersection(set2)
    length_common_set = len(common_set)
    return length_common_set


def set_differences(set1, set2):
    """counts the number of words that appear in one set and not another"""
    in1_not2 = set1.difference(set2)
    set_count = len(in1_not2)
    return set_count


def main():
    args = parser_directorypath()
    path_name = os.path.join(args.directorypath, "*c-darwin*")
    # finds the pathnames for any files that have *c-darwin* in the directory
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the c-darwin files found
    print(file_path_list)
    file1 = os.path.basename(file_path_list[0])
    # finds the basename for the first file path in the list created by glob
    total1 = total_words(file_path_list[0])
    file2 = os.path.basename(file_path_list[1])
    # finds the basename of the second file path in the list created by glob
    total2 = total_words(file_path_list[1])
    print("The total words in {} is {} and the total words in {} is {}.".format(file1, total1, file2, total2))
    os.chdir(args.directorypath)
    set1 = make_sets(file1)
    set2 = make_sets(file2)
    unique1 = count_unique_words(set1)
    unique2 = count_unique_words(set2)
    print("The following are the number of unique words in each file.\n{}\t{}\n{}\t{}".format(file1, unique1, file2, unique2))
    in_common = common_set(set1, set2)
    print("There are {} words in common between {} and {}.".format(in_common, file1, file2))
    set1_notset2 = set_differences(set1, set2)
    print("There are {} words that appear in {} that are not in {}.".format(set1_notset2, file1, file2))
    set2_notset1 = set_differences(set2, set1)
    print("There are {} words that appear in {} that are not in {}.".format(set2_notset1, file2, file1))


if __name__ == '__main__':
    main()
