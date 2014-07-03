#!/usr/local/bin/python

import sys, os, time, fnmatch

# Function for searching a directory for a file with correct matching.
def find(func, rootdir, **kw) :
	for file in os.listdir(rootdir) :
		filepath = os.path.join(rootdir, file)
		if os.path.islink(filepath) : 
			pass # Don't handle symbolic links!
		elif os.path.isdir(filepath) :
			find(func, filepath, **kw) # Enter each directory for processing.
		elif os.path.isfile(filepath) :
			func(filepath, **kw) # Handle each file in directory.
			
def writesize2(filename, extensions=['.*'], size_limit=1000000, age_limit=0, **kw) : 
	fileext = os.path.splitext(filename)[1] # Get extension of current file.
	treat_file = 0
	# Match for allowed extensions.
	for s in extensions :
		if fnmatch.fnmatch(fileext, s) : treat_file = 1

	# Handle matched extension file.
	if treat_file != 0 :
		size = os.path.getsize(filename) # Get file size.
		if size < size_limit : return
		cur_ftime = os.path.getmtime(filename) # Get modified time of file.
		cur_days = (cur_ftime / ( 60 * 60 * 24)) # Calculate days.
		now = time.time() / ( 60 * 60 * 24 ) # Calculate current days.
		if (now - cur_days) < age_limit : return
		
		# Give output information to user about matched files
		print "%gkb\tfile in %s" % ( (size/(1024), filename))
		print "\tlast modified %s" % time.asctime(time.gmtime(cur_ftime)) 
	
	
# Test program.	
try :
	test = sys.argv[1]
except :
	print "Nothing to find. Please give directory to search!", sys.exit(1)

print "Found the following file(s) matching search pattern : "
find(writesize2, test, size_limit = 1000, age_limit=7, extensions=['.py'])
