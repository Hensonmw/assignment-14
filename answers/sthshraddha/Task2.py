#! usr/bin/env python

"""
Assignment 14_Task2:
Credit url: https://automatetheboringstuff.com/chapter9/
Accesed on: 15 March, 2016

Created by Shraddha Shrestha on March 15, 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

import os
import argparse
import glob
import shutil


def get_parser():
    """Get directory information from user"""
    parser = argparse.ArgumentParser(
            description="""Getting access to files in user's directory input""")
    parser.add_argument(
            "--indir",
            required = True,
            type=str,
            help="""user's input directory address/path with files"""
        )
    parser.add_argument(
            "--outdir",
            required = True,
            type=str,
            help="""user's choice of output directory path for file_type sorted\
            files"""
        )
    return parser.parse_args()


def filtering_file_type(indir, outdir, file_type):
    my_files = glob.glob(os.path.join(indir, file_type))
    for file in my_files:
        shutil.copy(file, outdir)
        # copies the file sorted by file type in an output directory

def main():
    args = get_parser()
    filtering_file_type(args.indir, args.outdir, "*.fastq")


if __name__ == '__main__':
    main()
