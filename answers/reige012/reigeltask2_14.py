"""
Copy all fastq files from a specific directory into a new directory.

Edited by Alicia Reigel. 12 March 2016.
Copyright Alicia Reigel. Louisiana State University. 12 March 2016. All
rights reserved.

"""


import glob
import os
import argparse
import shutil


def parser_directorypath():
    """Collects the path of the directory where your files are"""
    parser = argparse.ArgumentParser(
        description="""Input the full path to the directory of interest"""
        )
    parser.add_argument(
            '--directorypath',
            required=True,
            type=str,
            help='Enter the path to the directory of interest.'
        )
    return parser.parse_args()


def make_file_copies(file_list, new_directorypath):
    """makes a copy of each file in the file list and puts it in the specified directory"""
    for file in file_list:
        shutil.copy(file, new_directorypath)


def main():
    args = parser_directorypath()
    path_name = os.path.join(args.directorypath, "*.fastq*")
    # finds the pathnames for any files that have *.fastq*
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the fastq files found
    mypath = os.path.join(args.directorypath + "/new_directorytask2")
    if not os.path.isdir(mypath):
        os.makedirs(mypath)
        # these last three lines create a new directory within the directorypath given in argparse
    path_to_new_directory = os.path.abspath(mypath)
    # gets the absolute path to the new directory created
    make_file_copies(file_path_list, path_to_new_directory)


if __name__ == '__main__':
    main()
