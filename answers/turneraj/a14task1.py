#!/usr/bin/env python
# encoding: utf-8

"""
 My first task for Assignment 14.

 Created by A.J. Turner on March 13, 2016. Helpful instructions/hints provided by S. Shakya. 
"""

import string
import os
import glob
import argparse
from collections import Counter

def get_location():
	""""user to input working directory"""
	parser = argparse.ArgumentParser()
	parser.add_argument("--directory", help="The path to your directory of interest", type=str)
	args = parser.parse_args()
	return args

def clean_file(myfiles):
	"""removing all punctuation from file"""
	for punct in string.punctuation: #developed by S. Shakya
		myfiles = myfiles.replace(punct, "")
	myfiles = myfiles.lower().replace("\n\n", " ").replace("\n", "").strip()
	return myfiles

def total_words(myfiles):
	"""obtain total words in file"""
	counting = len(myfiles.split())
	return counting


def uniq_word(myfiles):
	"""converting file into a set"""
	uniques = set(myfiles.split())
	return uniques


def main():
	args = get_location()
	file_in = glob.glob(os.path.join(args.directory, "*.txt")) #lists files in directory 
	#print(file_in) #to check directory files
	with open(file_in[0], "r") as run_file1: #using first file by indexing
		use_file1 = run_file1.read()
		clean_file1 = clean_file(use_file1)
		print("\n Total words for first file: ", total_words(clean_file1))
		uniqs1 = uniq_word(clean_file1)
		print("\n Unique words for first file: ",len(uniqs1))
		run_file1.close()
	with open(file_in[1], "r") as run_file2: #using second file by indexing
		use_file2 = run_file2.read()
		clean_file2 = clean_file(use_file2)
		print("\n Total words for second file: ", total_words(clean_file2))
		
		uniqs2 = uniq_word(clean_file2)
		print("\n Unique words for second file: ",len(uniqs2))
	print("\nThe number of words in chapter 1 that are also in chapter 2: ",len(uniqs1.intersection(uniqs2)))	
	print("\nThe number of words in chapter 1 that are not in chapter 2: ",len(uniqs1.difference(uniqs2)))
	print("\nThe number of words in chapter 2 that are not in chapter 1: ",len(uniqs2.difference(uniqs1)))
	

if __name__ == '__main__':
	main()