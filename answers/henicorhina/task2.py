# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
BIOL7800 assignment 14
Oscar Johnson 13 March 2016
"""

import argparse
import glob
import shutil
import os


def get_args():
    parser = argparse.ArgumentParser(
            description="""provide working directory for text files""")
    parser.add_argument('--input_dir',
                        type = str,
                        required = True,
                        help = "enter a directory containing text files to copy",
                        )
    parser.add_argument('--output_dir',
                        type = str,
                        required = True,
                        help = "enter an output directory where you want your files to go",
                        )
    return parser.parse_args()


def file_copier(in_path, out_path, file_type):
    """
    takes directory and copies all files of a specified type 
    to a new directory
    file_type = string of file names that you want copied    
    """
    filenames = glob.glob(os.path.join(in_path, file_type))
    #print(filenames) # should just be .fastq files
    for file in filenames:
        shutil.copy2(file, out_path)



def main():
    args = get_args()
    file_copier(args.input_dir, args.output_dir, "*.fastq")

if __name__ == '__main__':
    main()