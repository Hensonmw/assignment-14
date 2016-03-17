# !/usr/bin/env python
# encoding: utf-8


"""
My word-counting program
Created by Andre Moncrieff on 14 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import argparse
from collections import Counter
import os
import glob


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir_path", required=True,
                        help="Enter '--dir_path', space, and then the path" +
                        " of the directory containing the files of interest.",
                        type=str)
    args = parser.parse_args()
    return args


class WordCounter:
    def __init__(self, dir_path):
        # set things up
        self.dir_path = dir_path
        self.list_of_filenames = self.list_of_filenames(dir_path)
        self.file_object_1 = open(self.list_of_filenames[0], "r")
        self.file_object_2 = open(self.list_of_filenames[1], "r")

        # file 1 stuff
        self.word_list_1 = self.cleaned_up_word_list(self.file_object_1)
        self.word_set_1 = self.set_of_list(self.word_list_1)
        self.total_word_count_1 = self.word_count(self.word_list_1)
        self.word_count_dict = self.count_and_dictionate(self.word_list_1)
        self.all_punct_list_1 = self.cleaned_up_punct_list(self.file_object_1)
        self.punct_count_dict = self.count_and_dictionate(
                                self.all_punct_list_1)
        self.punct_set = self.set_of_list(self.all_punct_list_1)
        self.unique_word_count_1 = len(self.word_set_1)

        # file 2 stuff
        self.word_list_2 = self.cleaned_up_word_list(self.file_object_2)
        self.word_set_2 = self.set_of_list(self.word_list_2)
        self.total_word_count_2 = self.word_count(self.word_list_2)
        self.word_count_dict = self.count_and_dictionate(self.word_list_2)
        self.all_punct_list_2 = self.cleaned_up_punct_list(self.file_object_2)
        self.punct_count_dict = self.count_and_dictionate(
                                self.all_punct_list_2)
        self.punct_set = self.set_of_list(self.all_punct_list_2)
        self.unique_word_count_2 = len(self.word_set_2)

        # set stuff
        self.shared = len(self.word_set_1.intersection(self.word_set_2))
        self.in_1_not_2 = len(self.word_set_1.difference(self.word_set_2))
        self.in_2_not_1 = len(self.word_set_2.difference(self.word_set_1))

    def list_of_filenames(self, directory_path):
        os.chdir(directory_path)
        list_of_filenames = glob.glob("*.txt")
        return list_of_filenames

    def filename_by_index(self, num):
        return self.list_of_filenames[num]

    def cleaned_up_word_list(self, file_object):
        word_list = []
        punctuation = set("(),.?/!;:'\n\t")
        for line in file_object:
            if line != "\n":
                cleaned_line_0 = "".join(c for c in line if c not in
                                         punctuation)
                cleaned_line_1 = cleaned_line_0.casefold()
                parsed = cleaned_line_1.split(" ")
                word_list.extend(parsed)
        return word_list

    def word_count(self, word_list):
        total_word_count = len(word_list)
        total_word_count = total_word_count
        return total_word_count

    def cleaned_up_punct_list(self, file_object):
        punct_list = []
        letters_numbers = set(" \n\tABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn" +
                              "opqrstuvwxyz0123456789")
        for line in file_object:
            if line != "\n":
                cleaned_line = "".join(c for c in line if c not in
                                       letters_numbers)
                parsed = cleaned_line.split(" ")
                punct_list.extend(parsed)
        indiv_punct_list = []
        for item in punct_list:
            indiv_punct_list.extend(item)
        return indiv_punct_list

    def set_of_list(self, some_list):
        the_set = set(some_list)
        WordCounter.the_set = the_set
        return the_set

    def count_and_dictionate(self, some_list):
        word_count_dict = Counter(some_list)
        return word_count_dict

    def top_twenty(self, dictionary):
        top_twenty = dictionary.most_common(20)
        return top_twenty

    def top_ten(self, dictionary):
        top_ten = dictionary.most_common(10)
        return top_ten

    def display(self, some_dict):
        for item in some_dict:
            if len(item[0]) < 8:
                print("{}{}{}".format(item[0], "\t\t", item[1]))
            if len(item[0]) >= 8:
                print("{}{}{}".format(item[0], "\t", item[1]))
        print("{}".format("\n\n"))

def main():
    args = parser()
    word_master = WordCounter(args.dir_path)
    #print("List of Chapter 1 words: ", word_master.word_list_1)
    #print("List of Chapter 2 words: ", word_master.word_list_2)
    print("\n")
    print("The count of all words in Chapter 1: ",
          word_master.total_word_count_1)
    print("The count of unique words in Chapter 1: ",
          word_master.unique_word_count_1)
    print("The count of all words in Chapter 2: ",
          word_master.total_word_count_2)
    print("The count of unique words in Chapter 2: ",
          word_master.unique_word_count_2)
    print("The count of words in Chapter 1 that ARE in Chapter 2: ",
          word_master.shared)
    print("The count of words in Chapter 1 that ARE NOT in Chapter 2: ",
          word_master.in_1_not_2)
    print("The count of words in Chapter 2 that ARE NOT in Chapter 1: ",
          word_master.in_2_not_1)
    print("\n")

if __name__ == '__main__':
    main()
