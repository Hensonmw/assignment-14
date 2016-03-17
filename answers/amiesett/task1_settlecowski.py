#!/usr/bin/env python
# encoding: utf-8

"""
BIOL7800 Assignment 14 Task 1

Amie Settlecowski
16 Mar. 2016

Using word-counting class, WordCount, and sets to compare counts among text
files.

python task1_settlecowski.py --dir \path\to\directory\of\input_files\
"""


from collections import Counter
import argparse
import os
import glob


def get_args(parserr):
    '''
    Requires --dir flag for user to specify path to directory with input files
    '''
    parserr.add_argument("--dir",
        required=True,
        help="Path to directory with input files",
        type=str)


class WordCount():
    '''Counts the words of a file'''
    def __init__(self, file_name):
        '''Requisite attributes'''
        self.file_name = file_name
        self.file_path = os.path.abspath(file_name)
        self.master_word_tuple = self.construct_master()
        self.unique_words = set(self.master_word_tuple)

    def __str__(self):
        return '{}:\n words'.format(
                self.file_path)

    def construct_master(self):
        '''Construct master list of all words in file'''
        master_list = []
        # check that input file opens in read mode w/out error
        with open(self.file_name, 'r') as f:
            for line in f:
                word_list = self.process_line(line)
                master_list += (word for word in word_list)
        return tuple(master_list)

    def process_line(self, strng):
        '''
        Parse a string by spaces into a list of words
        '''
        strng = strng.lower().replace('\r\n', ' ')
        strng = strng.replace('  ', ' ').replace('   ', ' ').replace('-', ' ')
        new_strng = ''
        for character in strng:
            if character.isalpha() or character == ' ':
                new_strng += character
        list_of_words = new_strng.split(' ')
        return list_of_words

    def total(self):
        return len(self.master_word_tuple)

    def total_unique(self):
        return len(self.unique_words)

    def cnt(self, lst):
        '''Populate Counter cntr with occurrences of each item in lst'''
        cntr = Counter()
        for item in lst:
            cntr[item] += 1
        return cntr

    def display_counts(self, cntr, rank):
        '''Prints most common keys in a Counter (cntr) and their counts'''
        width = len(max(cntr, key=len))
        rank_counts = cntr.most_common(len(cntr.items()))
        n = 0
        for index in rank_counts:
            if n < rank:
                print('{0:{3}{width}}{2}{1:{3}}'.format(index[0], index[1],
                                                        '\t', '<', width=width))
            n += 1


def main():
    # creater Parser object with arguments for path to appropriate directory
    path_name_parser = argparse.ArgumentParser()
    get_args(path_name_parser)
    path_args = path_name_parser.parse_args()
    # change directory to appropriate directory
    os.chdir(path_args.dir)
    # Collect all text files and create WordCount object for each
    files = glob.glob('*.txt')
    chapter1 = WordCount(files[0])
    chapter2 = WordCount(files[1])

    intersect = chapter1.unique_words.intersection(chapter2.unique_words)
    not_in_2 = chapter1.unique_words.difference(chapter2.unique_words)
    not_in_1 = chapter2.unique_words.difference(chapter1.unique_words)

    print('{0:<28}{1:<}\n'.format('Total words in chapter 1:',
                                chapter1.total()))
    print('{0:<28}{1:<}\n'.format('Total words in chapter 2:',
                                chapter2.total()))
    print('{0:<28}{1:<}\n'.format('Unique words in chapter 1:',
                                chapter1.total_unique()))
    print('{0:<28}{1:<}\n'.format('Unique words in chapter 2:',
                                chapter2.total_unique()))
    print('{0:<28}{1:<}\n'.format('Shared words:', len(intersect)))
    print('{0:<28}{1:<}\n'.format('Words only in chapter 1:', len(not_in_2)))
    print('{0:<28}{1:<}\n'.format('Words only in chapter 2:', len(not_in_1)))

if __name__ == '__main__':
    main()
