import os
import glob
import logging
import config

from libs.codeparser import Parser
from libs.defgetter import defgetter


directory = os.path.abspath('demo_files')
filename = 'find.py'

os.chdir(directory)
dirlist = glob.glob('*')

for i in range(0, len(dirlist), 1):
    logging.debug('Found directory {}'.format(dirlist[i]))
    if not os.path.isdir(dirlist[i]):
        del dirlist[i]

if config.VERBOSE:
    print "Parsing all occurences of '" + filename + "'... ",
for stud in dirlist: # for each student in the supplied directory
    os.chdir(stud)
    if os.path.isfile(filename):
        if config.DEBUG: 
            print "\nReading "+stud+"s \'"+filename+"\' file. "
        p = Parser('python', open(filename, 'r'))
        kwh, oph, bigstring, bigstringhash, num_kw, num_op = p.parse_file()
        functions = defgetter('python', bigstring)
        if functions == None:
            print 'Trying to get functions, but language is unknown!'
            sys.exit(1)

        list_of_functions = functions

        # if config.DEBUG: 
        #     p.report_results(bigstring)
    os.chdir('..')
