import os
import glob
import logging
import config

from libs.codeparser import Parser
from libs.comparer import Comparer

from libs.assignment import Assignment

filename = 'demo_files/donny/helloworldplus.py'
filepath = os.path.abspath(filename)

print 'Open file', filename
filehandler = open(filepath, 'r')

assignment = Assignment(filename)

print 'Send filehandler to codeparser'
p = Parser('python', filehandler)
assignment.detektor_signature = p.get_code_signature()

print 'Returned code signature:'
from pprint import pprint
pprint(assignment.detektor_signature)


print
print
print '=' * 70
print
print assignment
print assignment.detektor_signature
print
print '=' * 70
print
print

programs = [assignment, assignment]
percentage = 20

c = Comparer(programs, percentage)
pprint(c.get_result())
# print c.build_result()

import sys
sys.exit()




################################################################################


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

        if config.DEBUG:
            p.report_results(bigstring)
    os.chdir('..')
