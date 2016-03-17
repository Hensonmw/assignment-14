# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 14
Oscar Johnson 13 March 2016
"""

import argparse
import collections
import glob
import os
import re


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide working directory for text files""")
    parser.add_argument('--directory',
                        type = str,
                        required = True,
                        help = "enter a folder containing text files with counts of words",
                        )
    return parser.parse_args()
    

def word_count(my_file):
    """get count of words from text file as dictionary Counter"""
    count_all = collections.Counter()
    word_list = []
    with open(my_file, 'r', encoding='utf-8') as my_text:
        for line in my_text:
            text = line.lower() #lowercase all text [^A-Za-z]
            text = re.sub("['-;:()&?!%,]", '', text) #remove non-alphanumeric chars
            text = re.sub("[\n]", '', text) #remove newlines
            text = re.sub('[.]', ' ', text) #replace periods with whitespace
            l = text.split() #listify
            # count of all words
            for word in l:
                count_all[word] += 1
                word_list.append(word)
    word_count = len(word_list)
    print("count of words in {}: {}".format(os.path.basename(my_file), word_count))
    #print(set(count)) # should be set of unique words
    set_count = set(word_list)
    print("count of unique words in {}: {}".format(os.path.basename(my_file), len(set_count)))
    #print(set_count)
    return set_count



def main():
    args = get_args()
    text_files = glob.glob(os.path.join(args.directory, "c-darwin-chapter-*.txt"))
    #files = file_getter(args.directory)
    chapter1 = word_count(text_files[0])
    chapter2 = word_count(text_files[1])
    #print(chapter1)
    #print(chapter2)
    intersection = chapter1.intersection(chapter2)
    diff = chapter1.difference(chapter2)
    diff2 = chapter2.difference(chapter1)
    print("the count of words in Chapter 1 that ARE in Chapter 2: ", len(intersection))
    print("the count of words in Chapter 1 that ARE NOT in Chapter 2: ", len(diff))
    print("the count of words in Chapter 2 that ARE NOT in Chapter 1: ", len(diff2))

if __name__ == '__main__':
    main()