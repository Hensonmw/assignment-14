# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:22:47 2016

@author: Marco
"""

import argparse
import glob
import os
import shutil


def parser_function():
    '''
    Function to parse arguments
    '''
    parser = argparse.ArgumentParser(description="""my argument parser""")
    # Adding an argument to 'parse'        
    parser.add_argument('in_folder', type=str, 
                        help='type the name of the folder from where you would'
                        ' like to copy the fastq files')
    parser.add_argument('out_folder', type=str, 
                        help='type the name of the folder where you would like'
                        ' paste the fastq files')
    args = parser.parse_args()
    inp = args.in_folder
    outp = args.out_folder
    return inp, outp


def os_globber(in_folder, out_folder):
    '''
    getting fastq files. This function uses the extra module "shutil".
    with this module I was able to copy stuff from one folder and past it into
    another
    '''
    list_of_files = glob.glob(in_folder+'/*.fastq')
    for file in list_of_files:
        basename = os.path.basename(file)
        shutil.copy(file, os.path.join(out_folder,basename))


def main():
    in_folder = parser_function()[0]
    out_folder = parser_function()[1]
    os_globber(in_folder, out_folder)
    

if __name__ == '__main__':
    main()