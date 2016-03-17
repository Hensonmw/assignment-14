#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
the total count of words in Chapter 1
the count of unique words in Chapter 1
the total count of words in Chapter 2
the count of unique words in Chapter 2
the count of words in Chapter 1 that ARE in Chapter 2
the count of words in Chapter 1 that ARE NOT in Chapter 2
the count of words in Chapter 2 that ARE NOT in Chapter 1
@author: York
'''

import os
import argparse
import glob
from collections import Counter


def get_args():
    parser = argparse.ArgumentParser(
        description="""Explode a directory of alignments into FASTA-formatted files for each locus or taxon""")
    parser.add_argument("--directory", type=str, help="""The path to a directory""")
    return parser.parse_args()
  
  
class Wordcounting:

    def __init__(self, filename):
        self.filename = filename
        self.read()


    def count_word(self):

        text1 = self.replace(",", " ").replace(".", " ")
        text2 = text1.replace("?", " ").replace("/", " ").replace("!", " ")
        text3 = text2.replace(":", " ").replace(";", " ").casefold()
        text4 = text3.replace(")", " ").replace(" (", " ")
        text5 = text4.replace("  ", " ")
        text6 = text5.split()
        counttext = Counter(text6)
        print(counttext)
        
  
def main():
    args = get_args()
    print("a=",args)
    my_files = glob.glob(os.path.join(args.directory, "*.txt"))
    print("b=",my_files)

    with open(my_files[0], "r") as inputfile1:
        inputfile_string1 = inputfile1.read()
    subst=inputfile_string1
    chapter1=set(Wordcounting.count_word(subst))
    print("chapter1=", chapter1)
    with open(my_files[1],"r") as inputfile2:
        inputfile_string2=inputfile2.read()
    subst1=inputfile_string2
    chapter2=set(Wordcounting.count_word(subst1))
    print("chapter2=", chapter2)
    print("c=",chapter1.intersection(chapter2))
    print(chapter1.difference(chapter2))
    print(chapter2.difference(chapter1))
    

if __name__ == '__main__':
    main()