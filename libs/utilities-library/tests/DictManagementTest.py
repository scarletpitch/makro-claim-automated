import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from UtilitiesLibrary import UtilitiesLibrary

testcase_utilities = UtilitiesLibrary()

class DictManageMentTest(unittest.TestCase):
    def test_verify_response_body(self):
        actual = {'data': 'Update All Resource', 'message': 'Function Put'}
        expect = {'data': 'Update All Resource', 'message': 'Function Put'}
        result = testcase_utilities.verify_response_body(actual, expect)
        self.assertIsNone(result)

    def test_update_data_into_original_dictionary(self):
        source = {'hello': 'to_override'}
        overrides = {'hello': 'over'}
        expect = {'hello': 'over'}
        result = testcase_utilities.update_data_into_original_dictionary(source, overrides)
        assert result == expect

    def test_convert_suds_object_to_dict(self):
        source = {'hello': 'to_override'}
        expect = {'hello': 'to_override'}
        result = testcase_utilities.convert_suds_object_to_dict(source)
        assert result == expect

    def test_update_the_value_for_the_key_list(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': 'null', 'transactionAmt': 'null'}
        key = {'accName'}
        value = 'H'
        expect = {'funcName': 'API123', 'appId': 222, 'accName': 'H', 'accNumber': 123456, 'accAmount': 'null', 'transactionAmt': 'null'}
        result = testcase_utilities.update_the_value_for_the_key_list(source,key,value)
        assert result == expect

    def test_update_the_value_for_selected_key(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': 'null','transactionAmt': 'null'}
        key = 'accName'
        value = 12345
        expect = {'funcName': 'API123', 'appId': 222, 'accName': 12345, 'accNumber': 123456, 'accAmount': 'null', 'transactionAmt': 'null'}
        result = testcase_utilities.update_the_value_for_selected_key(source, key, value)
        assert result == expect

    def test_get_the_value_for_selected_key(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': 'null','transactionAmt': 'null'}
        key = 'accName'
        expect = 'KBANK'
        result = testcase_utilities.get_the_value_for_selected_key(source, key)
        assert result == expect

    def test_get_list_diffs(self):
        source = {10, 15, 20, 25, 30, 35, 40}
        source2 = {25, 40, 35}
        expect = [10, 15, 20, 30]
        result = testcase_utilities.get_list_diffs(source, source2)
        assert result == expect

    def test_delete_key_in_dictionary(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': 'null','transactionAmt': 'null'}
        key = 'accNumber'
        expect = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accAmount': 'null', 'transactionAmt': 'null'}
        result = testcase_utilities.delete_key_in_dictionary(source, key)
        assert result == expect

    def test_update_value_from_original_dictionary(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': 'null','transactionAmt': 'null'}
        target = {'appId': None, 'accName': None}
        expect = {'appId': 222, 'accName': 'KBANK'}
        result = testcase_utilities.update_value_from_original_dictionary(source, target)
        assert result == expect

    def test_update_the_value_for_the_key_list_to_decimal(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': '1,234','transactionAmt': '3.14'}
        key = {'accAmount', 'amtTranfer'}
        # expect = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': Decimal('1234'), 'transactionAmt': '3.14'}
        result = testcase_utilities.update_the_value_for_the_key_list_to_decimal(source, key)
        print(result)

    def test_update_the_value_for_selected_key_to_decimal(self):
        source = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': '1,234','transactionAmt': 'null'}
        target = 'accAmount'
        # expect = {'funcName': 'API123', 'appId': 222, 'accName': 'KBANK', 'accNumber': 123456, 'accAmount': Decimal('1234'), 'transactionAmt': 'null'}
        result = testcase_utilities.update_the_value_for_selected_key_to_decimal(source, target)
        print(result)

    def test_validate_response_body(self):
        actual = {'data': 'Update All Resource', 'message': 'Function Put'}
        expect = {'data': 'Update All Resource', 'message': 'Function Put'}
        result = testcase_utilities.validate_response_body(actual, expect)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()