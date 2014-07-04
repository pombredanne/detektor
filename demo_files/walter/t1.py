#!/bin/sh
""":"
exec python $0 ${1+"$@"}
"""#"


import os

try:
    os.command("ls -l")
except:
    print 'Something went wrong'

class A:
    def __init__(self):
        print 'init running'
        print 'running and running'

    def hw(self):
        print 'hwdude'

def getbiggest():
    x = 1
    y = 2
    if x >= y:
        return x
    elif x <= y:
        return y
    print 'do the run run run'
    print 'or runaway'

import os

try:
    os.command("ls -l")
except:
    print "Could not run command"

print "This is a very simple test"


print 'kaller doi'
doi()
a = A()
a.howdy()
print 'program ferdig'
