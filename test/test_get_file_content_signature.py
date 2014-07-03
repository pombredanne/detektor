import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libs.codeparser import Parser

class GetPythonFileContentSignature(unittest.TestCase):

    def setUp(self):
        self.testfilehandler = open('test/pyfiles/find.py', 'r')

    def tearDown(self):
        self.testfilehandler.close()

    def testGetPythonContent(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, num_kw, num_op = p.parse_file()
        print kwh
        print oph
        print bigstring
        print num_kw
        print num_op


if __name__ == '__main__':
    unittest.main()
