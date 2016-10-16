#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 22:19:43 2016

@author: nikhilsable
"""

import sys

def pyfilereader(filename):
    f = open(filename, 'rU')
    lines = f.readlines()
    for line in lines:
        print line.split("\n")
    f.close()
    
def main():
    file = sys.argv[1]
    pyfilereader(file)
    


if __name__ == "__main__":
    main()