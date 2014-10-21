#!/usr/local/bin/python

import sys, os
from time import time, asctime, gmtime
from fnmatch import fnmatch

def find(proc, rootdir, **kw):
	""" Find files with suffix given """
	for file in os.listdir(rootdir) :
		filepath = os.path.join(rootdir, file)
		if os.path.islink(filepath) : 
			pass 
		elif os.path.isfile(filepath) :
			proc(filepath, **kw)
		elif os.path.isdir(filepath) :
			find(proc, filepath, **kw) 
			
def changed_writesize(filename, exts=['.*'],
	       sizelim=1000000,
	       agelim=0, **kw):
	""" Write the size of file to stdout """
	fileext = os.path.splitext(filename)[1] 
	filematch = 0
	for s in exts:
		if fnmatch(fileext, s):
			filematch = 1
	if filematch != 0:
		size = os.path.getsize(filename) 
		if size < sizelim : return
		cur_ftime = os.path.getmtime(filename)
		cur_days = (cur_ftime / ( 60 * 60 * 24))
		now = time() / ( 60 * 60 * 24 ) 
		if (now - cur_days) < agelim:
			return
		print "%gkb\tfile in %s" % ( (size/(1024), filename))
		print "\tlast modified %s" % asctime(gmtime(cur_ftime)) 
	

if not len(sys.argv) == 2:
	print 'Wrong number of arguments.'
	print 'Send root-dir as argument'
	sys.exit(0)
else:
	find(changed_writesize,
	     sys.argv[1],
	     sizelim = 1000,
	     agelim = 7,
	     exts = ['.py']
	     )
	

