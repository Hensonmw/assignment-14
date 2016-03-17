#!/usr/bin/env python
# encoding: utf-8

"""
 My third task for Assignment 14.

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
	args = parser.parse_args()
	return args


def integer(data):
	"""turning input into intergers"""
	return int(data)


def main():
	args = get_location()
	file_in = glob.glob(os.path.join(args.in_directory, "*.txt"))
	#print(file_in) #check to see if correct directory/files
	my_list = [] #placeholder 
	for file in file_in: #putting ints from a file into a list
		with open(file, "r") as myfiles:
			file_contents = myfiles.read()
			my_list.extend(file_contents.split(" ")) #putting list of ints from files into one big list
			myfiles.close()
	result = map(integer, my_list) #mapping mylist to use in the integer function above
	print("\nThe sum of integers from all files is: ", sum(list(result))) #sums list of ints and prints
			

if __name__ == '__main__':
	main()