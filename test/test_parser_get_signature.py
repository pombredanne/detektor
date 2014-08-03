import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libs.codeparser import Parser


class GetParserGetSignature(unittest.TestCase):

    def setUp(self):
        self.testfilehandler = open('test/pyfiles/helloworldplus.py', 'r')

    def tearDown(self):
        self.testfilehandler.close()

    def testGetPythonContentFileSignature(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertEqual(type(detektor_signature), dict)

    def testGetPythonContentFileSignatureHasBigstring(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('bigstring' in detektor_signature)

    def testGetPythonContentFileSignatureHasKeywordstring(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('keywordstring' in detektor_signature)

    def testGetPythonContentFileSignatureHasOperatorstring(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('operatorstring' in detektor_signature)

    def testGetPythonContentFileSignatureHasBigstringhash(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('bigstringhash' in detektor_signature)

    def testGetPythonContentFileSignatureHaslist_of_functions(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('list_of_functions' in detektor_signature)

    def testGetPythonContentFileSignatureHasnumber_of_keywords(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('number_of_keywords' in detektor_signature)

    def testGetPythonContentFileSignatureHasnumber_of_operators(self):
        p = Parser('python', self.testfilehandler)
        detektor_signature = p.get_code_signature()
        self.assertTrue('number_of_operators' in detektor_signature)
