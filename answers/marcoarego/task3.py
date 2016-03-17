# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 07:52:00 2016

@author: Marco
"""

import argparse
import glob


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'        
    parser.add_argument('in_folder', type=str, 
                        help='type the name of the folder from where you would'
                        ' like to copy the fastq files')
    args = parser.parse_args()
    inp = args.in_folder
    return inp


def get_files(my_path):
    final_list = []
    globber = glob.glob(my_path+'\*.txt')
    for my_file in globber:
        with open(my_file, 'r') as mine:
            for line in mine:
                final_list.append(line)
    return globber, final_list


def split_by_spaces(lis): return [x.split(" ") for x in lis]


def summarize(lis): return sum([int(x) for x in lis])


def main():
    inp = parser_function()
    globber, lista = get_files(inp)
    new_lis = split_by_spaces(lista)
    # Using map!!!
    maplist = list(map(summarize, new_lis))
    total_sum = sum(maplist)
    print("\nThis is the total sum: {}".format(total_sum))


if __name__ == '__main__':
    main()