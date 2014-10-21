import logging
from fabric.api import local


def test():
    import unittest
    logging.basicConfig(level=logging.DEBUG)
    testsuite = unittest.TestLoader().discover('detektor/tests')
    unittest.TextTestRunner(verbosity=1).run(testsuite)


def demo(num=0):
    num = int(num)
    if not num in (1, 2, 3, 4):
        print 'Choose demo 1, 2, 3 or 4. Run with e.g "fab demo:1"'
        return
    local('python demos/demo{}.py'.format(num))
