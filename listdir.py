#!/usr/bin/python3

import sys
import os
import argparse

argParser = argparse.ArgumentParser()

#Add arguments to the parser
argParser.add_argument("--index", "-i", help="Generate an index file containing all the files/folders in a directory.", action="store_true")
argParser.add_argument("--nlist", "-n", help="Do not list files in console.", action="store_true")
argParser.add_argument("--folder", "-f", help="Include folders.", action="store_true")

args = argParser.parse_args()

if args.index:
	file = open("index", "w")

for entry in os.scandir(os.getcwd()):
	if entry.is_dir() and not args.folder:			#Check if entry is folder and --folder arg is not specified. Continue if
		continue

	if args.index:									#Check if --index arg is specified. Write to it if it is.
		if not entry.name == "index":					#Only write if filename is not "index"
			file.write(entry.name + "\n")
	
	if not args.nlist:								#Check if --nlist arg is not specified. Print if
		print(entry.name)