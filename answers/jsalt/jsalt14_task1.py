#! usr/bin/env python
# encoding: utf-8

"""
Assignment 14
Task 1 Program: More word counts
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
        description='''Gets the input file path.'''
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Enter the path to the directory you want to work from.",
        type=str
    )
    return parser.parse_args()


def word_count(input_file):
    '''Reads the input file, formats the text into a list with each word as a
    string. Determines and prints the total word count for the text.'''
    with open(input_file, 'r') as doc:
        doc_string = doc.read()
    # This will include words with hyphens or apostrophes,
    # and numbers with decimals or commas:
    doc_list = re.findall(
                "\w+[,]\w+|\w+[.]\w+|\w+[-]\w+|[a-zA-z]+['][a-zA-Z]+|\w+",
                doc_string)
    full_list = [str.lower(word) for word in doc_list]
    formatted_list = list(filter(None, full_list))
    total_wc = len(formatted_list)
    filename = os.path.basename(input_file)
    print('There are {} words in {}.'.format(total_wc, filename))
    return formatted_list


def unique_words(total_wc):
    '''Determines and print the number of unique words in a text.'''
    unique_set = set(total_wc)
    unique_value = len(unique_set)
    print('{} of these are unique words.'.format(unique_value))
    return unique_set


def overlap(file1, file2, name1, name2):
    '''Determines and prints the number of overlapping and unique words between
    two files.'''
    overlap = len(file1 & file2)
    print('There are {} words that appear in both files.'.format(overlap))
    unique1 = len(file1 - file2)
    print(
          'There are {} words that appear in {} but not {}.'.format(
           unique1, name1, name2
          )
          )
    unique2 = len(file2 - file1)
    print(
          'There are {} words that appear in {} but not {}.'.format(
           unique2, name2, name1
          )
          )


def main():
    args = parser()
    # This takes care of the final / if the user forgot it:
    if args.input[-1] != '/':
        path_input = args.input + '/*'
    else:
        path_input = args.input + '*'
    work_dir = glob.glob(path_input)
    filename1 = os.path.basename(work_dir[0])
    filename2 = os.path.basename(work_dir[1])
    # I'm sure there's a neater way to do with using a for loop,
    # but I don't have time to work it out right now...
    total_words1 = word_count(work_dir[0])
    unique1 = unique_words(total_words1)
    total_words2 = word_count(work_dir[1])
    unique2 = unique_words(total_words2)
    overlap(unique1, unique2, filename1, filename2)


if __name__ == '__main__':
    main()
