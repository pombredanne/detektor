import os
import sys
from fabric.api import run, local

DETEKTOR = os.path.dirname(__file__)
os.environ.update({'DETEKTOR': DETEKTOR})

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test():
    import unittest
    testsuite = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=1).run(testsuite)

def demo(num=0):
    num = int(num)
    if not num in (1,2):
        print 'Choose demo 1 or 2. Run with e.g "fab demo:1"'
        return
    local('python demo{}.py'.format(num))
    