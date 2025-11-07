import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from UtilitiesLibrary import UtilitiesLibrary

testcase_utilities = UtilitiesLibrary()


class UtilitiesTest(unittest.TestCase):
    def test_verify_text_with_regEx(self):
        result = testcase_utilities.verify_text_with_regEx('test123', 'test123')
        expect = True
        assert result == expect

    def test_generate_request_uid(self):
        result = testcase_utilities.generate_request_uid('test')
        print(result)

if __name__ == '__main__':
    unittest.main()