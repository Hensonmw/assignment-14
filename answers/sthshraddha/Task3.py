#! usr/bin/env python

"""
Assignment 14_Task3:

Written without using map.
Tried many times without any success, so here is the script doing the same \
thing without using map :(

Created by Shraddha Shrestha on March 15, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

import os
import argparse
import glob


def get_parser():
    """Get directory information from user"""
    parser = argparse.ArgumentParser(
            description="""Getting access to files in user's directory input""")
    parser.add_argument(
            "--directory",
            required = True,
            type=str,
            help="""user's input directory with files, copy directory address/\
            path as a text (right click on directory)"""
        )
    return parser.parse_args()


def sum_of_integers(A):
    #my_files = glob.glob(os.path.join(args.directory, '*.txt'))
    total = 0
    #print(my_files)
    for file in A:
        #print(file)
        with open(file, 'r') as f:
            for line in f:
                for word in line.split():
                    #print(word)
                    total = total + int(word)
    return total


def main():
    args = get_parser()
    my_files = glob.glob(os.path.join(args.directory, '*.txt'))
    result = sum_of_integers(my_files)
    print(result)


if __name__ == '__main__':
    main()
