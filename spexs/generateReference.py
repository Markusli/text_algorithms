#!/usr/bin/env python

from sys import stdin,argv,stdout,exit
from random import shuffle
import optparse
import os

usage = "usage: %prog [options]"
version = "%prog 1.0"
description = "Generate reference by shuffling query sequences."
parser = optparse.OptionParser(usage=usage, version=version, description=description)
parser.add_option("-i", "--input", dest="input",
        help="Input query file (with counts)")
parser.add_option("-o", "--output", dest="output",
        help="Output file")
parser.add_option("-r", "--rep", dest="rep",default=0,
        help="If all counts are 1, how many times to shuffle one sequence (default 0 - take the count that is given).")
(options, args) = parser.parse_args()

rep = int(options.rep)

with open(options.input) as inFile:
    with open(options.output, 'w') as outFile:
        for line in inFile:
            line = line.split()
            if rep == 0:
                c = int(line[0])
            else:
                c = rep
            a = list(line[1].strip())
            for i in range(c):
                shuffle(a)
                outFile.write("1\t" + ''.join(a) + '\n')