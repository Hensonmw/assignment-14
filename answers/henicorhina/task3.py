# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 14
Oscar Johnson 13 March 2016
"""

import argparse
import glob
import math
import os


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide working directory for text files""")
    parser.add_argument('--input_dir',
                        type = str,
                        required = True,
                        help = "enter a directory containing text files to sum",
                        )
    return parser.parse_args()


def summing(l):
    """ l is a list"""
    return math.fsum(l)
    

def file_reader(path):
    """takes directory containing text files, 
    computes some of all integers in files"""
    filenames = glob.glob(os.path.join(path, "*.txt"))    
    my_list = []
    ints_list = []
    for file in filenames:
        with open(file, 'r') as my_file:
            for line in my_file:
                # split on spaces
                ints = line.split() 
                my_list.extend(ints)
    # convert strings to integers as new list
    ints_list = [int(val) for val in my_list]
    return summing(ints_list)
    # I cannot for the life of me get map() to work
    # the return function above calls the summing function just fun
    # I could also just do: return math.fsum(ints_list)
    #return list(map(summing, ints_list))



def main():
    args = get_args()
    result = file_reader(args.input_dir)
    print("sum of integers in files is: ", result)

if __name__ == '__main__':
    main()