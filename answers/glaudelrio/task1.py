#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 20:53:27 2016

@author: Glaucia
"""

import re
import argparse
import os
import glob


def arguments():
        """parsing arguments to allow changing input file and output name"""
        parser = argparse.ArgumentParser(description="""my argument parser""")   
        parser.add_argument('directoryname', type=str, help="""give the entire name of the directory 
                                                      containing your files""")
        args = parser.parse_args()
        args = args.directoryname
        return args


class Counting_Words:
    """a class that allows counting the punctuation and ammount of words in a text"""
    
    def __init__(self,filename,secondtextfilename):
         self.filename = filename
         self.filepath = os.path.abspath("self.filename")
         self.totalwords = str(len(self.amountofwords()))
         self.numberofuniquewords = str(len(self.uniquewords()))
         self.secondtext = secondtextfilename
         self.totalwordssecondtext = str(len(self.amountofwordssecondtext()))
         self.numberofuniquewordssecondtext = str(len(self.uniquewordssecondtext()))
         self.wordsincommon = str(len(self.intersection()))
         self.onlyinone = str(len(self.onlyinone()))
         self.onlyintwo = str(len(self.onlyintwo()))
         
    
    def openningfile(self,filename):
        """opens a text file whose name is given as input in the shell. Returns a string that will be used
        in word counts"""
        storingfile = []
        with open(self.filename,'r') as my_file:
            for line in my_file:
                storingfile.append(line)  
            text = "".join(storingfile)
        return text
    
    def openningsecondfile(self,secondtext):
        """opens a text file whose name is given as input in the shell. Returns a string that will be used
        in word counts"""
        storingfile = []
        with open(self.secondtext,'r') as my_file:
            for line in my_file:
                storingfile.append(line)  
            text = "".join(storingfile)
        return text
    
    def dealingtext (self):
        """edits a string removing ponctuation, spaces new lines, and capital letters
        to allow adequate word count. Returns the edited string"""
        text = self.openningfile(self.filename)
        text = re.sub("'","",text)
        text = re.sub('"',"",text)
        text = re.sub("\n","",text)
        text = re.sub("\W"," ",text)
        text = re.sub("\s+"," ",text)
        text = re.sub("-"," ",text)
        text = text.lower()
        finaltext = text.strip()
        return finaltext
    
    def dealingsecondtext (self):
        """edits a string removing ponctuation, spaces new lines, and capital letters
        to allow adequate word count. Returns the edited string"""
        text = self.openningsecondfile(self.secondtext)
        text = re.sub("'","",text)
        text = re.sub('"',"",text)
        text = re.sub("\n","",text)
        text = re.sub("\W"," ",text)
        text = re.sub("\s+"," ",text)
        text = re.sub("-"," ",text)
        text = text.lower()
        finaltext = text.strip()
        return finaltext
    
    def amountofwords(self):
        """counts the words in the string provided in the last two functions, writes a file 
        with all the word counts (tab delimited). The argument filename takes the name of the file
        that will be writen. Returns a dictionary with all the words counts"""
        finaltext = self.dealingtext()
        wordlist = finaltext.split(" ")
        return wordlist
    
    def amountofwordssecondtext(self):
        """counts the words in the string provided in the last two functions, writes a file 
        with all the word counts (tab delimited). The argument filename takes the name of the file
        that will be writen. Returns a dictionary with all the words counts"""
        finaltext = self.dealingsecondtext()
        wordlist = finaltext.split(" ")
        return wordlist
        
    def uniquewords(self):
        """counts the amount of unique words in one chapter"""
        wordlist = self.amountofwords()
        self.unique1 = set(wordlist)
        return self.unique1
    
    def uniquewordssecondtext(self):
        """counts the amount of unique words in the other chapter"""
        wordlist = self.amountofwordssecondtext()
        self.unique2 = set(wordlist)
        return self.unique2
        
    def intersection(self):
        """counts the amount of words in common in both chapters"""
        wordsincommon = self.unique1.intersection(self.unique2)
        return wordsincommon
        
    def onlyinone(self):
        """counts the amount of words present only in chapter 1"""
        differentwords = self.unique1.difference(self.unique2)
        return differentwords
    
    def onlyintwo(self):
        """counts the amount of words present only in chapter 2"""
        differentwords = self.unique2.difference(self.unique1)
        return differentwords
    
            
def main():
    arg = arguments()
    files = glob.glob(arg + "/*.txt")
    mydocuments = Counting_Words(files[0],files[1])
    print("First file unique words: " + mydocuments.numberofuniquewords)
    print("First file total number of words " + mydocuments.totalwords)
    print("Second file unique words: " + mydocuments.numberofuniquewordssecondtext)
    print("Second file total number of words: " + mydocuments.totalwordssecondtext) 
    print("Count of words in Chapter 1 that ARE in Chapter 2: " + mydocuments.wordsincommon)
    print("Count of words in Chapter 1 that ARE NOT in Chapter 2: " + mydocuments.onlyinone)
    print("Count of words in Chapter 2 that ARE NOT in Chapter 1: " + mydocuments.onlyintwo)
    
           
if __name__ == '__main__':
    main()      