#!/usr/bin/env python
# utf-8

"""
Assignment 14, Task 1
Jon Nations on 12 March 2016
This takes 2 chapters of "On the Origin of Species" and
turns them to sets, counts words, unique words, and compares them
"""
import argparse
import glob
import os
import re


def file_in():
    """gets input directory containint text files"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, type=str, help="give input directory where c-darwin-chapter# files are stored")
    # parser.add_argument('--output', required=True, help='give output file')
    return parser.parse_args()


def chapter1(my_files):
    with open(my_files[0], 'r') as mychuck:
        clean = mychuck.read()
        clean = clean.lower()
        clean = re.sub('[-]', ' ', clean)  # removes hyphens in words
        clean = re.sub(r'\s+', ' ', clean)  # condense all whitespace
        clean = re.sub('[^A-Za-z ]+', '', clean)  # remove non-alpha chars
        # print(clean) for debugging
        # regular expressions from gist.github.com/bradmontgomery
        # clean = re.sub('^[^t].+', '', clean)
        clean_chuck = clean.split()
        print('\nChapter 1 has a total of ' + str(len(clean_chuck)) + ' words,')
        chuck_set1 = set(clean_chuck)
        print('and contains ' + str(len(chuck_set1)) + ' unique words\n')
        return chuck_set1


def chapter2(my_files):
    with open(my_files[1], 'r') as mychuck:
        clean = mychuck.read()
        clean = clean.lower()
        clean = re.sub('[-]', ' ', clean)  # removes hyphens in words
        clean = re.sub(r'\s+', ' ', clean)  # condense all whitespace
        clean = re.sub('[^A-Za-z ]+', '', clean)  # remove non-alpha chars
        # regular expressions from gist.github.com/bradmontgomery
        clean_chuck = clean.split()
        print('Chapter 2 has a total of ' + str(len(clean_chuck)) + ' words,')
        chuck_set2 = set(clean_chuck)
        print('and contains ' + str(len(chuck_set2)) + ' unique words\n')
        return chuck_set2


def main():
    file_in()
    args = file_in()
    my_files = glob.glob(os.path.join(args.directory, "*.txt"))
    # I am assuming this produces a list of files called "my_files"
    c_set1 = chapter1(my_files)
    c_set2 = chapter2(my_files)
    """the count of words in Chapter 1 that ARE in Chapter 2
    the count of words in Chapter 1 that ARE NOT in Chapter 2
    the count of words in Chapter 2 that ARE NOT in Chapter 1"""
    same = len(c_set1.intersection(c_set2))
    print("Chapters 1 and 2 share {0} words\n".format(same))
    diff1 = len(c_set1.difference(c_set2))
    print("Chapter 1 has {0} words that are not in Chapter 2\n".format(diff1))
    diff2 = len(c_set1.difference(c_set1))
    print("Chapter 2 has {0} words that are not in Chapter 1. How is that possible??\n".format(diff2))
    c_set1.issubset(c_set2)

if __name__ == '__main__':
    main()
