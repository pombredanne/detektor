import os
import glob
import logging
import config

from libs.defgetter import defgetter # a helper module for Python src

from libs.codeparser import Parser

directory = os.path.abspath('demo_files/donny')
filepath = os.path.join(directory, 'find.py')

if os.path.isfile(filepath):
    p = Parser('python', open(filepath, 'r'))
    kwh, oph, bigstring, bigstringhash, num_kw, num_op = p.parse_file()
    functions = defgetter('python', bigstring)
    p.report_results(bigstring)
    for function in functions:
        print function
