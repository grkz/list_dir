#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from os.path import join, getsize, isdir

# if no argument provided -> list current dir
if len(sys.argv) < 2:
	dir = '.'
else:
	dir = sys.argv[1]

def get_dirsize(path):
	"""Calculates the size of all files in specified dir and it's subdirs.
	4096 bytes (linux) are added for compatibility with du -b ..path..""" # node size?
	size = 0.0
	for top, dirs, files in os.walk(path):
		size += sum(getsize(join(top, f)) for f in files + dirs)
		#print top, size
	return size + getsize(path) # compatibility with du -b for folders (du adds 


file_sizes = []
for f in os.listdir(dir):
	file_path = join(dir, f)
	if isdir(file_path):	# if a file is a directory, calculate it's total size
		print f, "(dir)", get_dirsize(file_path)
		file_sizes.append((f, get_dirsize(file_path)))
		
	else:			# append filename and size to the list of results
		print f, getsize(file_path)
		file_sizes.append((f, getsize(file_path)))
# sort by size:
file_sizes.sort(key=lambda x: x[1], reverse=True) # sort by size from each tuple
print "The largest file/dir in '" + dir + "': " + str(file_sizes[0][0]) + " size: " + str(file_sizes[0][1])
