# !/usr/bin/env python
# encoding: utf-8


"""
My file-copying program
Created by Andre Moncrieff on 14 March 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""


import argparse
import os
import glob
import shutil


def parser():
    """
    Create argument input
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--curr_dir_path", required=True,
                        help="Enter '--curr_dir_path', space, and then the" +
                        " path of the directory containing the files of" +
                        "interest.",
                        type=str)
    parser.add_argument("--new_dir_path", required=True,
                        help="Enter '--new_dir_path', space, and then the" +
                        " path of the directory into which you want to copy" +
                        " the files.",
                        type=str)
    args = parser.parse_args()
    return args


class FileMover:
    def __init__(self, curr_dir_path, new_dir_path):
        # set things up
        self.curr_dir_path = curr_dir_path
        self.new_dir_path = new_dir_path
        self.list_of_filenames = self.list_of_filenames(self.curr_dir_path)

    def list_of_filenames(self, curr_dir_path):
        os.chdir(curr_dir_path)
        list_of_filenames = glob.glob("*.fastq")
        return list_of_filenames

    def copy_files(self):
        for fastq_filename in self.list_of_filenames:
            shutil.copy(fastq_filename, self.new_dir_path)


def main():
    args = parser()
    file_master = FileMover(args.curr_dir_path, args.new_dir_path)
    file_master.copy_files()


if __name__ == '__main__':
    main()
