import unittest
import mock
from detektor.parseresultcomparer import ParseResultCompareTwo, ParseResultCompareMany


class TestParseResultComparer(unittest.TestCase):

    def test_compare_operators_and_keywords_string_equal_nomatch(self):
        a = mock.MagicMock()
        a.get_operators_and_keywords_string.return_value = 'a'
        b = mock.MagicMock()
        b.get_operators_and_keywords_string.return_value = 'b'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_operators_and_keywords_string_equal(),
            None)

    def test_compare_operators_and_keywords_string_equal(self):
        a = mock.MagicMock()
        a.get_operators_and_keywords_string.return_value = 'x'
        b = mock.MagicMock()
        b.get_operators_and_keywords_string.return_value = 'x'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_operators_and_keywords_string_equal(),
            'operators_and_keywords_string_equal')

    def test_compare_operators_string_equal_nomatch(self):
        a = mock.MagicMock()
        a.get_operators_string.return_value = 'a'
        b = mock.MagicMock()
        b.get_operators_string.return_value = 'b'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_operators_string_equal(),
            None)

    def test_compare_operators_string_equal(self):
        a = mock.MagicMock()
        a.get_operators_string.return_value = 'x'
        b = mock.MagicMock()
        b.get_operators_string.return_value = 'x'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_operators_string_equal(),
            'operators_string_equal')

    def test_compare_keywords_string_equal_nomatch(self):
        a = mock.MagicMock()
        a.get_keywords_string.return_value = 'a'
        b = mock.MagicMock()
        b.get_keywords_string.return_value = 'b'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_keywords_string_equal(),
            None)

    def test_compare_keywords_string_equal(self):
        a = mock.MagicMock()
        a.get_keywords_string.return_value = 'x'
        b = mock.MagicMock()
        b.get_keywords_string.return_value = 'x'
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_keywords_string_equal(),
            'keywords_string_equal')

    def test_compare_total_operatorcount_equal_nomatch(self):
        a = mock.MagicMock()
        a.get_number_of_operators.return_value = 10
        b = mock.MagicMock()
        b.get_number_of_operators.return_value = 20
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_total_operatorcount_equal(),
            None)

    def test_compare_total_operatorcount_equal(self):
        a = mock.MagicMock()
        a.get_number_of_operators.return_value = 5
        b = mock.MagicMock()
        b.get_number_of_operators.return_value = 5
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_total_operatorcount_equal(),
            'total_operatorcount_equal')

    def test_compare_total_keywordcount_equal_nomatch(self):
        a = mock.MagicMock()
        a.get_number_of_keywords.return_value = 10
        b = mock.MagicMock()
        b.get_number_of_keywords.return_value = 20
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_total_keywordcount_equal(),
            None)

    def test_compare_total_keywordcount_equal(self):
        a = mock.MagicMock()
        a.get_number_of_keywords.return_value = 5
        b = mock.MagicMock()
        b.get_number_of_keywords.return_value = 5
        self.assertEqual(
            ParseResultCompareTwo(a, b)._compare_total_keywordcount_equal(),
            'total_keywordcount_equal')



class TestParseResultCompareMany(unittest.TestCase):
    def test_compare_many(self):
        parseresult1 = mock.MagicMock()
        parseresult1.get_operators_and_keywords_string = 'x'
        parseresult2 = mock.MagicMock()
        parseresult2.get_operators_and_keywords_string = 'x'
        parseresult2.get_number_of_operators = 10
        parseresult3 = mock.MagicMock()
        parseresult3.get_operators_and_keywords_string = 'y'
        parseresult3.get_number_of_operators = 10
        comparemany = ParseResultCompareMany([parseresult1, parseresult2, parseresult3])
        comparemany.sort_by_points_descending()
        for comparetwo in comparemany:
            print comparetwo
