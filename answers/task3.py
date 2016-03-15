#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:48:13 2016

@author: Glaucia
"""
import argparse
import re
import glob


def arguments():
        """parsing arguments to have input file"""
        parser = argparse.ArgumentParser(description="""my argument parser""")   
        parser.add_argument('inputdirectoryname', type=str, help="""give the entire name of the directory 
                                        (and path) containing your files""")                                          
        args = parser.parse_args()
        inp = args.inputdirectoryname
        return inp


def sumnumbersinalist (inputfile):
        """gets and input file, reads and edits it, and sum across the integer values in this file"""
        numberslist = []
        with open(inputfile,'r') as my_file:
            for line in my_file:
                numberslist.append(line)
        numbers = "".join(numberslist)
        numbers = re.sub("\W"," ",numbers)
        finalnumbers = numbers.strip()
        finalnumbers = finalnumbers.split(" ")
        numlist = list(map(int,finalnumbers))
        return sum(numlist)
       

def main():
    arg = arguments()
    mainresult = sum(list(map(sumnumbersinalist,glob.glob(arg +"/*.txt"))))
    print(mainresult)
     
               
if __name__ == '__main__':
    main()   
