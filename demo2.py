import os
import glob
import logging
import config

from libs.codeparser import Parser
from libs.defgetter import defgetter
from libs.comparer import Comparer

from libs.assignment import Assignment


directory = os.path.abspath('demo_files')
filename = 'helloworldplus.py'

filepath = os.path.abspath('demo_files/donny/helloworldplus.py')

print 'Open file "demo_files/donny/helloworldplus.py"'
filehandler = open(filepath, 'r')

print 'Send filehandler to codeparser'
p = Parser('python', filehandler)

codedata = p.get_code_signature()

print 'Returned code signature:'
from pprint import pprint
pprint(codedata)

codedata.update({'list_of_functions': defgetter('python', codedata.get('bigstring'))})

assignment = Assignment(**codedata)

print
print
print '='*70
print
print assignment
print
print '='*70
print
print

programs = [assignment, assignment]
percentage = 20

c = Comparer(programs, percentage)
pprint(c.get_result())
# print c.build_result()






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
