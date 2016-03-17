#!/usr/bin/env python
# encoding: utf-8

"""
 My second task for Assignment 14.

 Created by A.J. Turner on March 14, 2016. Helpful instructions/hints provided by S. Shakya. 
"""

import string
import os
import glob
import argparse

def get_location():
	""""user to input working directory"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--in_directory", help="The path to your input directory of interest", type=str)
	parser.add_argument("--out_directory", help="The path to your output directory of interest (make one)", type=str)
	args = parser.parse_args()
	return args

	
def main():
	args = get_location()
	file_in = glob.glob(os.path.join(args.in_directory,"*.fastq")) #directory with fastqs
	#print(file_in) #checks to see if you isolated fastq
	for file in file_in:
		with open(os.path.join(args.in_directory, os.path.basename(file)), "r") as myfile:
			file_contents = myfile.read()
		with open(os.path.join(args.out_directory, os.path.basename(file)), "w") as copyfile:
			copyfile.write(file_contents)
			copyfile.close()


if __name__ == '__main__':
	main()