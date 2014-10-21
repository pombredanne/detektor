import os
import sys
from fabric.api import local

DETEKTOR = os.path.dirname(__file__)
os.environ.update({'DETEKTOR': DETEKTOR})
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test():
    import unittest
    testsuite = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=1).run(testsuite)


def demo(num=0):
    num = int(num)
    if not num in (1, 2, 3, 4):
        print 'Choose demo 1, 2, 3 or 4. Run with e.g "fab demo:1"'
        return
    local('python demos/demo{}.py'.format(num))
