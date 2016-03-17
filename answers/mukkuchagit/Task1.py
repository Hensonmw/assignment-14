#!/usr/bin/env python
# encoding: utf-8
"""
assignment 14.

Copyright 2016 Mukesh Maharjan. All rights reserved.
"""
import glob
import argparse
import re


def blunt_word(filename):
    input_file = open(filename)
    read_file = input_file.read()
    read_file = re.sub(r'[^\w\s\n\n]', ' ', read_file)
    wordstring = read_file.replace("\n", "").replace("  ", " ").casefold()
    return wordstring


def count_all(filename):
    input_file = open(filename, 'r')
    count = 0
    for x in input_file.read().split():
        count += 1
    input_file.close()
    return count


def count_unique(wordstring):

    word_list = wordstring.split()
    unique_list = set(word_list)
    return len(unique_list)


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_pattern", help="Enter Input File Extention after '*' ")
    pattern = parse.parse_args()
    file_list = glob.glob(pattern.input_pattern)

    total_word_count = count_all(file_list[0])
    print('The total number of words in ' + file_list[0] +' is: ' + str(total_word_count))

    wordstring = blunt_word(file_list[0])
    unique_word_count = count_unique(wordstring)
    print('The total number of unique words in ' + file_list[0] +' is: ' + str(unique_word_count))

    total_word_count = count_all(file_list[1])
    print('The total number of words in ' + file_list[1] +' is: ' + str(total_word_count))

    wordstring = blunt_word(file_list[1])
    unique_word_count = count_unique(wordstring)
    print('The total number of unique words in ' + file_list[1] +' is: ' + str(unique_word_count))


    wordstring1 = blunt_word(file_list[0])
    wordstring2 = blunt_word(file_list[1])
    set1=set(wordstring1.split())
    set2 = set(wordstring2.split())

    print('The total number of common words in ' + file_list[0] +' and ' + file_list[1] + ' are:' + str(len(set1.intersection(set2))))
    print('The total number of words in ' + file_list[0] +' but not in ' + file_list[1] + ' are:' + str(len(set1.difference(set2))))
    print('The total number of words in ' + file_list[1] +' but not in ' + file_list[0] + ' are:' + str(len(set2.difference(set1))))


if __name__ == '__main__':
    main()
