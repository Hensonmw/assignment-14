#!/usr/bin/env python
# utf-8

"""
Program for task1 of assignment 14
Created by Pramod Pantha on 15 March, 2016.
Copyright 2016 Pramod Pantha. All right reserved.
"""


from collections import Counter
import argparse
import glob
import os


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help='the path to a directory', type=str)
    # parser.add_argument("--inputfile2", required=True)
    args = parser.parse_args()

    return args


def lowercase_replace(string):
    text1 = string.replace(",", " ").replace(".", " ")
    text2 = text1.replace("?", " ").replace("/", " ").replace("!", " ")
    text3 = text2.replace(":", " ").replace(";", " ").casefold()
    text4 = text3.replace(")", " ").replace(" (", " ")
    text5 = text4.replace("  ", " ")
    text6 = text5.split()
    return text6


def text_count(l):
        counttext = Counter(l)
        return counttext


def words_count(d):
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
    a = lowercase_replace(inputfile_string1)
    b = text_count(a)
    words_count(b)
    chapter1 = uniq_count_word(b)
    print(chapter1)
    with open(file1[1], "r", encoding='utf-8') as inputfile2:
        inputfile_string2 = inputfile2.read()
    d = lowercase_replace(inputfile_string2)
    e = text_count(d)
    words_count(e)
    chapter2 = uniq_count_word(e)
    print(chapter2)
    print(chapter1.intersection(chapter2))
    print(chapter1.difference(chapter2))
    print(chapter2.difference(chapter1))


if __name__ == '__main__':
    main()
