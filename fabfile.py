import os
import sys
from fabric.api import run

DETEKTOR = os.path.dirname(__file__)
os.environ.update({'DETEKTOR': DETEKTOR})

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test():
    import unittest
    testsuite = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
