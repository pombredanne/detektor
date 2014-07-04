#!/bin/sh
""":"
exec python $0 ${1+"$@"}
"""#"

import os

try:
    os.command("ls -l")
except:
    print 'Something went wrong'

class Big_stuff:
    def __init__(self):
        print 'init running'
        print 'running and running'

    def howdy(self):
        print 'go gorilla'

def biggest():
    x = 1
    y = 2
    if x >= y:
        return x
    elif y >= x:
        return y
    print 'do the run run run'


import os

try:
    os.command("ls -l")
except:
    print "Could not run command"

print "This is a very simple test"

def doi():
    a = 1
    b = 2
    if a <= b:
        print 'go'
    elif b <= a:
        print 'gogo'
    elif a == b:
        print 'feck!'

class B:
    def __init__(self):
        print 'init'
        a = 1
        if a == 0:
            return 1
        else:
            return None

    def foops(self):
        print 'gofy'
        return 0

print 'kaller doi'
doi()
a = A()
a.howdy()
b = B()
b.foops()
print 'program ferdig'
