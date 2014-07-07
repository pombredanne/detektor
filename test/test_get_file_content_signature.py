import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libs.codeparser import Parser

class GetPythonFileContentSignature(unittest.TestCase):

    def setUp(self):
        self.testfilehandler = open('test/pyfiles/helloworldplus.py', 'r')

    def tearDown(self):
        self.testfilehandler.close()

    def testGetPythonContentKeywordString(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(kwh, '_0_0_0_0_0_1_0_0_0_0_0_0_0_0_0_0_1_0_0_0_0_0_0_2_0_1_0_0_0')

    def testGetPythonContentOperatorString(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(oph, '_0_2_0_0_0_1_0_0_0_0_0_0_0_0_0_0_0_0_0_0')

    def testGetPythonContentBigstring(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(bigstring_hash, -7070753577415992373)

    def testGetPythonContentNumberOfKeywords(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(num_kw, 5)

    def testGetPythonContentNumberOfOperators(self):
        self.assertIsInstance(self.testfilehandler, file)
        p = Parser('python', self.testfilehandler)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(num_op, 3)


if __name__ == '__main__':
    unittest.main()
