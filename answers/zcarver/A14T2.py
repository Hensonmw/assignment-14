#! /usr/bin/env python
# encoding UTF-8

'''
Assignment14Task2 biol7800
ZacCarver 03/15/2016
In the directory task2-files, there are a lot of files. Write a program that
uses argparse, glob, and os to copy only the fastq files to a new directory.
Your program should contain a main loop and an ifmain statement,
it should be formatted correctly, and you should take both the input directory
containing the files you want to copy and the output directory where you will
copy the files as arguments on the command-line.
'''

import argparse
import glob
import os
import shutil


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--start_dir", type=str, required=True,
                        help="enter directory to copy files")
    parser.add_argument("--des_dir", type=str, required=True,
                        help="provide destination directory for copied files")
    return parser.parse_args()


def cpyto(start_dir, des_dir):
    files = glob.glob(os.path.join(start_dir, '*.fastq'))
    for f in files:
        if os.path.isfile(f):
            shutil.copy2(f, des_dir)


def main():
    arg = args()
    cpyto(arg.start_dir, arg.des_dir)

if __name__ == '__main__':
    main()
