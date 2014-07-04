""" Get detektor signature for code in a given file.

Opens the file 'demo_files/donny/find.py' and sends this to the detektor codeparser.

Prints misc info.
"""

import os
import glob
import logging
import config

from libs.defgetter import defgetter
from libs.codeparser import Parser

filepath = os.path.abspath('demo_files/donny/find.py')

print 'Open file "demo_files/donny/find.py"'
filehandler = open(filepath, 'r')

print 'Send filehandler to codeparser'
p = Parser('python', filehandler)

codedata = p.get_code_signature()

print 'Returned code signature:'
from pprint import pprint
pprint(codedata)

if config.VERBOSE:
    functions = defgetter('python', codedata['bigstring'])
    p.report_results(codedata['bigstring'])
    for function in functions:
        print function
