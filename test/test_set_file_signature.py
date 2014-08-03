import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libs.codeparser import Parser


def get_deep_attr(obj, attrs):
    for attr in attrs.split("."):
        obj = getattr(obj, attr)
    return obj


def has_deep_attr(obj, attrs):
    try:
        get_deep_attr(obj, attrs)
        return True
    except AttributeError:
        return False


class Fass(object):
    path = 'test/pyfiles/helloworldplus.py'

    def __repr__(self):
        return self.path


class Ass(object):
    f = None
    a = 100

    def __init__(self):
        self.f = Fass()


class TestSetSignatureOnObject(unittest.TestCase):

    def setUp(self):
        self.testfilehandler = open('test/pyfiles/helloworldplus.py', 'r')

    def tearDown(self):
        self.testfilehandler.close()

    def test1(self):
        a = Ass()

        print '***', has_deep_attr(a, 'f.path')
        filepath = get_deep_attr(a, 'f.path')
        print '###', filepath

        f = open(filepath, 'r')
        self.assertIsInstance(f, file)
        p = Parser('python', f)
        kwh, oph, bigstring, bigstring_hash, num_kw, num_op = p.parse_file()
        self.assertEqual(kwh, '_0_0_0_0_0_1_0_0_0_0_0_0_0_0_0_0_1_0_0_0_0_0_0_2_0_1_0_0_0')


if __name__ == '__main__':
    unittest.main()
