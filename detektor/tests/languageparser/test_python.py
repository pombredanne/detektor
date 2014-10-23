import unittest
from detektor.languageparser.python import PythonLanguageParser


class TestPythonLanguageParser(unittest.TestCase):

    def test_keywords_sanity(self):
        self.assertEquals(
            PythonLanguageParser('print "Hello world"').parse().keywords,
            ['print'])
        self.assertEquals(
            PythonLanguageParser('if x == 10: pass').parse().keywords,
            ['if', 'pass'])
        self.assertEquals(
            PythonLanguageParser('while True: pass').parse().keywords,
            ['while', 'pass'])
        self.assertEquals(
            PythonLanguageParser('for x in [1, 2]: pass').parse().keywords,
            ['for', 'in', 'pass'])

    def test_operators_sanity(self):
        self.assertEquals(
            PythonLanguageParser('a == 10').parse().operators,
            ['=='])
        self.assertEquals(
            PythonLanguageParser('a==10').parse().operators,
            ['=='])
        self.assertEquals(
            PythonLanguageParser('a <>10').parse().operators,
            ['<>'])
        self.assertEquals(
            PythonLanguageParser('a > 10').parse().operators,
            ['>'])
