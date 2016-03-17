# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:04:16 2016

@author: Marco
"""

import argparse
import glob
import os
import re


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'        
    parser.add_argument('in_folder', type=str, 
                        help='type the name of the folder you would like to get'
                        ' the txt files to count words')
    args = parser.parse_args()
    inp = args.in_folder
    return inp


class TextReader:
    def __init__(self,filename):
        self.filename = filename
        self.filepath = os.path.abspath("self.filename")

    def file_opener(self,filename):
        '''
        Opens and transform a txt file in to a string
        '''
        my_list = []   
        with open(self.filename,'r') as darwin:
            for line in darwin:
                item = re.sub("\s+"," ",line)
                my_list.append(item.strip())
        for my_string in my_list:
            if len(my_string) == 0:
                my_list.pop(my_list.index(my_string))
        my_fused_string = ' '.join(my_list)
        return my_fused_string

    def string_standizer(self):
        '''
        this function takes all kinds of pontuation out of our string, including
        the apostrophe (') of words like can't, for example. The output will
        comprehend a lower case string with words separated by spaces.
        '''
        low = self.file_opener(self.filename).casefold()
        new_lines_out = re.sub("\n"," ",low)
        without_apos = re.sub("'","",new_lines_out)
        without_pontuation = re.sub("\W"," ",without_apos)
        one_space = re.sub("\s+"," ",without_pontuation)
        end_stripper = one_space.strip()
        return end_stripper

    def total_word_count(self):
        '''
        Counts total number of words in a txt document
        '''
        standard_text = self.string_standizer()
        wordlist = standard_text.split(" ")
        return len(wordlist), wordlist

    def unique_words(self):
        '''get a set of words'''
        return set(self.total_word_count()[1])

    def len_uni_wds(self):
        '''get length of unique words'''
        return len(self.unique_words())


def main():
    file_path = parser_function()
    # using glob!!!
    file1 = glob.glob(file_path+'/*1.txt')[0]
    file2 = glob.glob(file_path+'/*2.txt')[0]
    chapter1 = TextReader(file1)
    total_count_1 = chapter1.total_word_count()[0]
    uniq_count_1 = chapter1.len_uni_wds()
    set1 = chapter1.unique_words()
    chapter2 = TextReader(file2)
    total_count_2 = chapter2.total_word_count()[0]
    uniq_count_2 = chapter2.len_uni_wds()
    set2 = chapter2.unique_words()
    inter = len(set1.intersection(set2))
    diff1 = len(set1.difference(set2))
    diff2 = len(set2.difference(set1))
    print("\nChapter 1 total word count: {}\n"
    "Chapter 1 unique word count: {}\n"
    "Chapter 2 total word count: {}\n"
    "Chapter 2 unique word count: {}\n"
    "Count of words in Chapter 1 that ARE in Chapter 2: {}\n"
    "Count of words in Chapter 1 that ARE NOT in Chapter 2: {}\n"
    "Count of words in Chapter 2 that ARE NOT in Chapter 1: {}"
    .format(total_count_1, uniq_count_1, total_count_2, uniq_count_2, inter,
            diff1, diff2))


if __name__ == '__main__':
    main()