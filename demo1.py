""" Get detektor signature for code in a given file.

Opens the file 'demo_files/donny/helloworldplus.py' and sends this to the
detektor codeparser.

The file looks like this:

    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    a = 1
    print '%s + %s equals %s' % (a, a, add(a, a))

Prints misc info.
"""

import os
import glob
import logging
import config

from libs.defgetter import defgetter
from libs.codeparser import Parser

filepath = os.path.abspath('demo_files/donny/helloworldplus.py')

print 'Open file "demo_files/donny/helloworldplus.py"'
filehandler = open(filepath, 'r')

print 'Send filehandler to codeparser'
p = Parser('python', filehandler)

codedata = p.get_code_signature()

print 'Returned code signature:'
from pprint import pprint
pprint(codedata)

if config.VERBOSE or True:
    functions = defgetter('python', codedata['bigstring'])
    p.report_results(codedata['bigstring'])
    for function in functions:
        print function
