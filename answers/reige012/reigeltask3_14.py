"""
Read in files from a directory and add all of the integer values together using
map().

Edited by Alicia Reigel. 12 March 2016.
Copyright Alicia Reigel. Louisiana State University. 12 March 2016. All
rights reserved.

"""


import os
import glob
import argparse


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


def read_file_make_list(file):
        with open(file, 'r') as string:
            the_string = string.read()
            value_list = the_string.split()
            return value_list


def main():
    args = parser_directorypath()
    path_name = os.path.join(args.directorypath, "*.txt")
    # finds the pathnames for any files that have *.fastq*
    file_path_list = glob.glob(path_name)
    # creates a list of the path names associated with the fastq files found
    f1 = read_file_make_list(file_path_list[0])
    f2 = read_file_make_list(file_path_list[1])
    f3 = read_file_make_list(file_path_list[2])
    f4 = read_file_make_list(file_path_list[3])
    f5 = read_file_make_list(file_path_list[4])
    f6 = read_file_make_list(file_path_list[5])
    f7 = read_file_make_list(file_path_list[6])
    f8 = read_file_make_list(file_path_list[7])
    f9 = read_file_make_list(file_path_list[8])
    f10 = read_file_make_list(file_path_list[9])
    list_of_lists = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10
    result = list(map(int, list_of_lists))
    # had some help figuring this one out (credit: Amie Settlecowski)
    thesum = sum(result)
    print("The sum of all of the values in the ten files is:", thesum)


if __name__ == '__main__':
    main()
