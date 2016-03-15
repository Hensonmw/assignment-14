#!/usr/bin/env python
# utf-8

"""
Assignment 14, Task 2
Jon Nations on 12 March 2016
"""

import argparse
import glob
import os


def file_in():
    """gets input directory containint text files"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--directory', required=True, type=str, help="give input directory where all files are stored")
    parser.add_argument('-o', '--output_dir', required=True, help="give output directory where fastq files will be stored")
    # parser.add_argument('--output', required=True, help='give output file')
    return parser.parse_args()


def main():
    file_in()
    args = file_in()
    my_files = glob.glob(os.path.join(args.directory, "*.fastq"))
    # print(my_files) for debuging
    os.makedirs(args.output_dir)
    for file in my_files:
        with open(os.path.join(args.directory, os.path.basename(file)), 'r') as infile:
            files = infile.read()
        with open(os.path.join(args.output_dir, os.path.basename(file)), 'w') as        out:
            out.write(files)
            out.close()


if __name__ == '__main__':
    main()
