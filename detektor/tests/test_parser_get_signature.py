import os
import sys
import unittest
from cStringIO import StringIO

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from detektor.libs.codeparser import Parser


class GetParserGetSignatureSanity(unittest.TestCase):

    def setUp(self):
        self.testfilehandler = StringIO("""import os

def add(a, b):
    return a + b

print 'Hello %s!' % 'world'
a = 1
print '%s + %s equals %s' % (a, a, add(a, a))
        """)
        p = Parser('python', self.testfilehandler)
        self.detektor_signature = p.get_code_signature()

    def testGetPythonContentFileSignature(self):
        self.assertEqual(type(self.detektor_signature), dict)

    def testGetPythonContentFileSignatureHasBigstring(self):
        self.assertTrue('bigstring' in self.detektor_signature)

    def testGetPythonContentFileSignatureHasKeywordstring(self):
        self.assertTrue('keywordstring' in self.detektor_signature)

    def testGetPythonContentFileSignatureHasOperatorstring(self):
        self.assertTrue('operatorstring' in self.detektor_signature)

    def testGetPythonContentFileSignatureHasBigstringhash(self):
        self.assertTrue('bigstringhash' in self.detektor_signature)

    def testGetPythonContentFileSignatureHaslist_of_functions(self):
        self.assertTrue('list_of_functions' in self.detektor_signature)

    def testGetPythonContentFileSignatureHasnumber_of_keywords(self):
        self.assertTrue('number_of_keywords' in self.detektor_signature)

    def testGetPythonContentFileSignatureHasnumber_of_operators(self):
        self.assertTrue('number_of_operators' in self.detektor_signature)


class GetParserGetSignaturePythonDetails(unittest.TestCase):

    def test_empty_file(self):
        testfilehandler = StringIO('')
        p = Parser('python', testfilehandler)
        signature = p.get_code_signature()
        self.assertEquals(signature['number_of_keywords'], 0)
        self.assertEquals(signature['number_of_operators'], 0)

    def test_keywords(self):
        testfilehandler = StringIO('print "hello world"\nif a == 20')
        p = Parser('python', testfilehandler)
        signature = p.get_code_signature()
        print(signature)
        self.assertEquals(signature['number_of_keywords'], 2)

    def test_operators(self):
        testfilehandler = StringIO('a == 10 and b > 20 or c < 30')
        p = Parser('python', testfilehandler)
        signature = p.get_code_signature()
        print(signature)
        self.assertEquals(signature['number_of_operators'], 3)

    def test_bigstring(self):
        testfilehandler = StringIO('print "hello world"\nif a == 20')
        p = Parser('python', testfilehandler)
        signature = p.get_code_signature()
        self.assertEquals(signature['bigstring'], 'printif==')

    def test_only_function(self):
        testfilehandler = StringIO('def test(): pass')
        p = Parser('python', testfilehandler)
        signature = p.get_code_signature()
        print signature
        # self.assertEquals(signature['number_of_keywords'], 0)
        # self.assertEquals(signature['number_of_operators'], 0)

