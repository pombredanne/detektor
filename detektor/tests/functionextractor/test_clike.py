import unittest
import mock
from detektor.functionextractor.clike import ClikeFunctionExtractor


class TestClikeFunctionExtractor(unittest.TestCase):

    def test_something(self):
        keywords = {
            'if', 'while'
        }
        functions = ClikeFunctionExtractor(keywords).extract("""
            void main(int i) {
                // Some code here
            }

            int[] test() {
            }

            Array<String> anotherTest() {
                if(i == 10) {
                    while(true) {
                        print("Something");
                    }
                }
            }
        """)
        for functionname, sourcecode in functions:
            print '-' * 70
            print functionname
            print sourcecode
