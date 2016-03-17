#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:24:21 2016

@author: Glaucia
"""

import argparse
import glob
import shutil
import os

def arguments():
        """parsing arguments to allow changing input file and output file"""
        parser = argparse.ArgumentParser(description="""my argument parser""")   
        parser.add_argument('inputdirectoryname', type=str, help="""give the entire name of the directory 
                                        (and path)containing your files""")
        parser.add_argument('outputdirectoryname', type=str, help="""give the entire name (and path)
                                        of the directory you want to put your files""")                                              
        args = parser.parse_args()
        inp = args.inputdirectoryname
        out = args.outputdirectoryname
        return inp,out


def copyfastqfiles(inputfile,outputfile):
        """ a function that copies the fastq file from an input file to an output file, just remember that the
        inpu and output must contain the entire path """
        for filename in glob.glob(os.path.join(inputfile + "/*.fastq")):
            shutil.copy(filename, outputfile)


def main():
    arg1 = arguments()[0]
    arg2 = arguments()[1]
    copyfastqfiles(arg1,arg2) 
    
           
if __name__ == '__main__':
    main()   
