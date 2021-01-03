#!/usr/bin/python3

import sys
import os
import argparse

argParser = argparse.ArgumentParser()

#Add arguments to the parser
argParser.add_argument("-i", "--index", help="Generate an index file containing all the files/folders in a directory.", action="store_true")
argParser.add_argument("-n", "--nlist", help="Do not list files in console.", action="store_true")
argParser.add_argument("-f", "--folder", help="Include folders.", action="store_true")
argParser.add_argument("-p", "--path", help="Path to use. Will use working directory if not specified.")

args = argParser.parse_args()

#Set directory variable
if args.path:
	directory = args.path
else:
	directory = os.getcwd()

#Check if directory is valid
if not os.path.exists(directory):
	print("Directory specified does not exist. Try again!")
	sys.exit(1)

#Open index file if --index arg is specified.
if args.index:
	file = open("index", "w")

for entry in os.scandir(directory):
	if entry.is_dir() and not args.folder:			#Check if entry is folder and --folder arg is not specified. Continue if
		continue

	if args.index:									#Check if --index arg is specified. Write to it if it is.
		if not entry.name == "index":					#Only write if filename is not "index"
			file.write(entry.name + "\n")
	
	if not args.nlist:								#Check if --nlist arg is not specified. Print if
		print(entry.name)