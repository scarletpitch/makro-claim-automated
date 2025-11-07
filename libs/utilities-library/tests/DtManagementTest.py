import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from UtilitiesLibrary import UtilitiesLibrary

testcase_utilities = UtilitiesLibrary()

class DTManageMentTest(unittest.TestCase):
    def test_get_now_datetime(self):
        result = testcase_utilities.get_now_datetime()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}:\d{2}$'
        self.assertRegex(result, regex)

    def test_get_now_datetime_iso(self):
        result = testcase_utilities.get_now_datetime_iso()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z'
        self.assertRegex(result, regex)

    def test_get_now_total_seconds(self):
        result = testcase_utilities.get_now_total_seconds()
        print(result)

    def test_get_current_date_with_local_timezone(self):
        result = testcase_utilities.get_current_date_with_local_timezone()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}$'
        self.assertRegex(result, regex)

    def test_convert_epoch_to_date_and_time(self):
        data = 1575339570
        expect = "(None, '09:19:30 AM')"
        result = testcase_utilities.convert_epoch_to_date_and_time(data)
        str_result = str(result)
        assert str_result == expect

    def test_get_iso_datetime_tzcus(self):
        result = testcase_utilities.get_iso_datetime_tzcus()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{4}$'
        self.assertRegex(result, regex)

    def test_get_utc_datetime(self):
        actual = testcase_utilities.get_utc_datetime()
        regex = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}$'
        self.assertRegex(actual, regex)

    def test_get_iso_datetime_ml(self):
        actual = testcase_utilities.get_iso_datetime_ml()
        regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}\+\d{2}:\d{2}$'
        self.assertRegex(actual, regex)

if __name__ == '__main__':
    unittest.main()