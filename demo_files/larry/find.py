#!/usr/local/bin/python

from time import time, asctime, gmtime
from fnmatch import fnmatch
import sys, os

def find(proc,rootdir,**kw):
	# Find the files with the given type
	for file in os.listdir(rootdir) :
		filepath = os.path.join(rootdir, file)
		if os.path.islink(filepath) :
			# Not to be treated
			pass 
		elif os.path.isfile(filepath) :
			# Send the file to a given proc
			proc(filepath, **kw)
		elif os.path.isdir(filepath) :
			# Call find rekursively, since a dir is found
			find(proc, filepath, **kw) 
			
def writesize(filename, exts=['.*'], sizelim=1000000, agelim=0, **kw):
	# print the file data to terminal
	fileext = os.path.splitext(filename)[1] 
	filematch = 0
	for s in exts:
		# Test for match on every extension given
		if fnmatch(fileext, s):
			filematch = 1
	if filematch != 0:
		# get the size of the file
		size = os.path.getsize(filename)
		# if the file is not big enough,
		# nothing more should be done
		if size < sizelim: return
		# get the last modification date for file
		cur_ftime = os.path.getmtime(filename)
		# change from seconds to normal time
		cur_days = (cur_ftime / ( 60 * 60 * 24))
		now = time() / ( 60 * 60 * 24 )
		# if it's not old enough, do no more
		if (now - cur_days) < agelim: return
		print "%gkb\tfile in %s" % ( (size/(1024), filename))
		print "\tlast modified %s" % asctime(gmtime(cur_ftime)) 
	

if not len(sys.argv) == 2:
	print 'No dir-name given'
	print 'Try again'
	sys.exit(1)
else:
	find(writesize, sys.argv[1], sizelim = 1000,
	     agelim = 7, exts = ['.py'] )


