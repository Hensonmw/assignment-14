#!/usr/bin/env python
# encoding: utf-8
"""
created by me for task1 to open and read these chapters and some other code to
get a list of all words in each chapter
"""
from collections import Counter
import argparse
import glob
import os


def get_parser():
    """
   using argparse to takes the list  as input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help='directory to use', type=str)
    # parser.add_argument("--inputfile2", required=True)
    args = parser.parse_args()

    return args


def lowercase_replace(string):
    """
    remove, and change all characters to lower case, count the frequency
    words
    """

    text1 = string.replace(",", " ").replace(".", " ")
    text2 = text1.replace("?", " ").replace("/", " ").replace("!", " ")
    text3 = text2.replace(":", " ").replace(";", " ").casefold()
    text4 = text3.replace(")", " ").replace(" (", " ")
    text5 = text4.replace("  ", " ")
    text6 = text5.split()
    # mylist.extend(text6)
    # return mylist
    return text6


def count_text(l):
        counttext = Counter(l)
        return counttext


def count_words(d):
    """
    sort and formatted all the words in tab-delimited format
    """
    sorted_dict = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for i in sorted_dict:
        if len(i[0]) < 8:
            print("{0}\t{1}\n".format(i[0], i[1]))
        if len(i[0]) >= 8 and len(i[0]) < 16:
            print("{0}\t{1}\n".format(i[0], i[1]))
        if len(i[0]) >= 16:
            print("{0}\t{1}\n".format(i[0], i[1]))


def uniq_count_word(arg):
    my_set = set(arg)
    return(my_set)


def main():
    args = get_parser()
    file1 = glob.glob(os.path.join(args.directory, "*.txt"))
    print(file1)
    with open(file1[0], "r") as inputfile1:
        inputfile_string1 = inputfile1.read()
    A = lowercase_replace(inputfile_string1)
    B = count_text(A)
    count_words(B)
    chapter1 = uniq_count_word(B)
    print(chapter1)
    with open(file1[1], "r", encoding='utf-8') as inputfile2:
        inputfile_string2 = inputfile2.read()
    D = lowercase_replace(inputfile_string2)
    E = count_text(D)
    count_words(E)
    chapter2 = uniq_count_word(E)
    print(chapter2)
    print(chapter1.intersection(chapter2))
    print(chapter1.difference(chapter2))
    print(chapter2.difference(chapter1))


if __name__ == '__main__':
    main()
