#! /usr/bin/env python
# encoding: utf-8

'''
Grace Cagle
14 March 2016
Assignment 14 Task 1

A program that uses argparse and glob to open and read these chapters and some
other code to get a list of all words in each chapter. Ouputs the following:

    the total count of words in Chapter 1
    the count of unique words in Chapter 1
    the total count of words in Chapter 2
    the count of unique words in Chapter 2
    the count of words in Chapter 1 that ARE in Chapter 2
    the count of words in Chapter 1 that ARE NOT in Chapter 2
    the count of words in Chapter 2 that ARE NOT in Chapter 1
    the count of words in Chapter 2 that ARE NOT in Chapter 1
'''
import argparse
import string
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
    return(list_of_files)


def word_count(somefile):
    exclude = set(string.punctuation)
    with open(somefile, 'r') as f:
        my_input = f.read()
        remove_ch = ''.join(ch for ch in my_input if ch not in exclude)
        make_list = remove_ch.lower().replace('\n', ' ').split(' ')
        return make_list


def compare_files(ch1, ch2):
    set1 = set(ch1)
    set2 = set(ch2)
    ch1notin2 = str(len(set1.difference(set2)))
    ch2notin1 = str(len(set2.difference(set1)))
    ch1andin2 = str(len(set1.intersection(set2)))
    return(ch1andin2, ch2notin1, ch1notin2)


def main():
    args = get_args()
    list_of_files = read_directory(args)
    file1 = list_of_files[0]
    file2 = list_of_files[1]
    ch1 = word_count(file1)
    ch2 = word_count(file2)
    print("The total number of words in chapter 1:{}".format(len(ch1)))
    print("The number of unique words in chapter 1:{}".format(len(set(ch1))))
    print("The total number of words in chapter 2: {}".format(len(ch2)))
    ch1 = word_count(file1)
    ch2 = word_count(file2)
    t = compare_files(ch1, ch2)
    print('In chapter 1 and 2: {}\nIn chapter 2 not in 1: {}\nIn chapter 1 and \
    not 2: {}'.format(*t))


if __name__ == '__main__':
    main()
