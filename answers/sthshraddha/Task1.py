#!/usr/bin/env python

"""
Assignment_14:Task1
Using argparse and glob to open and read text chapters to get list of all words\
in each chapter.

Created by Shraddha Shrestha on March 15, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.
"""

import string
from collections import Counter
import glob
import os
import argparse
import re


def get_parser():
    """Get directory information from user"""
    parser = argparse.ArgumentParser(
            description="""Getting access to files in user's directory input""")
    parser.add_argument(
            "--directory",
            required = True,
            type=str,
            help="""user's input directory with files, copy directory address/\
            path as a text (right click on directory)"""
        )
    return parser.parse_args()


def get_wordlist_from_text_file(file):
    # removing all the possible punctuation marks in the input file
    input_list = re.split('\W+', file)
    formatted_list = [str.lower(word) for word in input_list]
    return formatted_list


def count_words(arg):
    total_words_count_dict = Counter(arg)
    #print(total_words_count_dict)
    total = 0
    for x in total_words_count_dict:
        #print(total_words_count_dict[x])
        total = total + total_words_count_dict[x]
    return total


def get_unique_words(arg):
    unique_words_count = Counter(set(arg))
    total = 0
    for x in unique_words_count:
        total = total + unique_words_count[x]
    return total


def making_sets_from_string(formatted_list):
    set_file = set(formatted_list)
    return set_file


def finding_common_set(set1, set2):
    common_set = set1.intersection(set2)
    common_set_length = len(common_set)
    return common_set_length


def finding_different_set(set1, set2):
    different_set = set1.difference(set2)
    different_set_length = len(different_set)
    return different_set_length


def main():
    args = get_parser()
    my_files = glob.glob(os.path.join(args.directory, '*.txt'))
    # my_files is just a string of pathname
    with open (my_files[0], 'r') as inputfile1:
        inputfile_string1 = inputfile1.read()
        allwords1 = get_wordlist_from_text_file(inputfile_string1)
        B = count_words(allwords1)
        print("\nTotal words count in Chapter 1 is:\n", B)
        #print("Total words count in text file2:\n", B)
        C = get_unique_words(allwords1)
        print("\nTotal unique words count in Chapter 1 is: \n", C)
    with open (my_files[1], 'r') as inputfile2:
        inputfile_string2 = inputfile2.read()
        allwords2 = get_wordlist_from_text_file(inputfile_string2)
        D = count_words(allwords2)
        print("\nTotal words count in Chapter 2 is:\n", D)
        E = get_unique_words(allwords2)
        print("\nTotal unique words count in Chapter 2 is: \n", E)
    set1 = making_sets_from_string(allwords1)
    set2 = making_sets_from_string(allwords2)
    common_count = finding_common_set(set1, set2)
    print("\nThe count of words in Chapter 1 that are in Chapter 2 as well is: \n", common_count)
    different_count1 = finding_different_set(set1, set2)
    print("\nThe count of words in Chapter 1 that are NOT in Chapter 2 is: \n", different_count1)
    different_count2 = finding_different_set(set2, set1)
    print("\nThe count of words in Chapter 2 that are NOT in Chapter 1 is: \n", different_count2)


if __name__ == '__main__':
    main()
