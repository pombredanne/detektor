#!/usr/local/bin/python
import os, sys, fnmatch, time


####################### function: report ####################################
def report(file, suffix=['.*'], max_size=1000000, min_age=0, **kw):
	# first we want to get the extension of the specified file
	extension = os.path.splitext(file)[1]
	# A temp variable used as boolean
	tmp_bool = 0
	
	# Match for allowed suffix.
	for suf in suffix:
		
		if fnmatch.fnmatch(extension, suf):
			# if the match the extension
			tmp_bool = 1

	if tmp_bool != 0:
		# Get the size of the file:
		size = os.path.getsize(file) 
		if size < max_size:
			return
		# Get the time for last modification
		modified_time = os.path.getmtime(file)
		# Convert the time to date
		cur_days = (modified_time / ( 60 * 60 * 24)) 
		today = time.time() / ( 60 * 60 * 24 ) 
		if (today - cur_days) < min_age:
			return
		
		# report result for this file
		print "%gkb\tis the size of %s" % ( (size/(1024), file))
		print ("\tThe last modification was done %s\n" % (
			time.asctime(time.gmtime(modified_time)) ))
#############################################################################	
	


####################### function: find ######################################
def find(function, folder, **specs):
	for file in os.listdir(folder):
		this_file = os.path.join(folder, file)
		if os.path.islink(this_file):
			# if the file is a symlink, just ignore
			pass
		elif os.path.isdir(this_file):
			# recursive call for found directory
			find(function, this_file, **specs) 
		elif os.path.isfile(this_file):
			# call the given function for action on this file
			function(this_file, **specs)
#############################################################################

			

############################### main ########################################
# check if argument is given
try:
	dir = sys.argv[1]
# if no argument is given, notify and exit
except:
	print 'Usage:',sys.argv[1],'directory'
	sys.exit(1)
print 'The files that matched the given pattern was:'
find(report, dir, max_size = 1000, min_age=7, suffix=['.py'])


