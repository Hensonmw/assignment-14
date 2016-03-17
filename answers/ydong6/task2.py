#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Mar 15, 2016 In the directory task2-files, there are a lot of files.
Write a program that uses argparse, glob, and os to copy only the fastq files to
a new directory. Your program should contain a main loop and an ifmain
statement, it should be formatted correctly, and you should take both the input
directory containing the files you want to copy and the output directory where
you will copy the files as arguments on the command-line. 
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
    parser.add_argument("--output", type=str, help="""output file""")
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
        
def file_out(args, my_files):
    my_fastqs = str(copy.deepcopy(my_files))
    print(my_fastqs)
    os.makedirs(args.output_dir)


def main():
    args = get_args()
    print("a=",args)
    my_files = glob.glob(os.path.join(args.directory, "*.fastq"))
    print("b=",my_files)

    with open(my_files[0], "r") as inputfile1:
        inputfile_string1 = inputfile1.read()
    subst=inputfile_string1
    file_out(subst)

if __name__ == '__main__':
    main()