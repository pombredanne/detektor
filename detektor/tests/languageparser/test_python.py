import unittest
from detektor.languageparser.python import PythonLanguageParser


class TestPythonLanguageParser(unittest.TestCase):

    def test_keywords_sanity(self):
        parser = PythonLanguageParser()

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'print "Hello world"')
        self.assertEquals(parseresult.keywords, ['print'])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'if x == 10: pass')
        self.assertEquals(parseresult.keywords, ['if', 'pass'])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'while True: pass')
        self.assertEquals(parseresult.keywords, ['while', 'pass'])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'for x in [1, 2]: pass')
        self.assertEquals(parseresult.keywords, ['for', 'in', 'pass'])

    def test_operators_sanity(self):
        parser = PythonLanguageParser()

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a == 10')
        self.assertEquals(parseresult.operators, ['=='])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a==10')
        self.assertEquals(parseresult.operators, ['=='])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a*10')
        self.assertEquals(parseresult.operators, ['*'])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a ==10')
        self.assertEquals(parseresult.operators, ['=='])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a== 10')
        self.assertEquals(parseresult.operators, ['=='])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a > 10')
        self.assertEquals(parseresult.operators, ['>'])

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a <> 10')
        self.assertEquals(parseresult.operators, ['<>'])
