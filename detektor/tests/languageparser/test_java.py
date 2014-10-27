import unittest
from detektor.languageparser.java import JavaLanguageParser


class TestJavaLanguageParser(unittest.TestCase):

    def test_keywords_sanity(self):
        parser = JavaLanguageParser()

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'if(true)')
        self.assertEquals(parseresult.keywords['if'], 1)
        for keyword in parser.keywords:
            if keyword != 'if':
                self.assertEquals(parseresult.keywords[keyword], 0)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'if(x == 10) return')
        self.assertEquals(parseresult.keywords['if'], 1)
        self.assertEquals(parseresult.keywords['return'], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'while(true) return')
        self.assertEquals(parseresult.keywords['while'], 1)
        self.assertEquals(parseresult.keywords['return'], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'for(int x: somelist) return')
        self.assertEquals(parseresult.keywords['for'], 1)
        self.assertEquals(parseresult.keywords['int'], 1)
        self.assertEquals(parseresult.keywords['return'], 1)

    def test_operators_sanity(self):
        parser = JavaLanguageParser()

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a == 10')
        self.assertEquals(parseresult.operators['=='], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a==10')
        self.assertEquals(parseresult.operators['=='], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a*10')
        self.assertEquals(parseresult.operators['*'], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a ==10')
        self.assertEquals(parseresult.operators['=='], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a== 10')
        self.assertEquals(parseresult.operators['=='], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a > 10')
        self.assertEquals(parseresult.operators['>'], 1)

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, 'a != 10')
        self.assertEquals(parseresult.operators['!='], 1)

    def test_functions(self):
        parser = JavaLanguageParser()

        parseresult = parser.make_parseresult()
        parser.parse(parseresult, '''
        public class Test {
            public void main(String[] args) {
                printHello();
            }

            private void printHello() {
                System.out.println("Hello World!");
            }
        }
        ''')
        for functionresult in parseresult.parsed_functions:
            print functionresult.label
            print functionresult
        # self.assertEquals(parseresult, 1)
