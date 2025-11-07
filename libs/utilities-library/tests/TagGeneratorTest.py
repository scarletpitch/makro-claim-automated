import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from UtilitiesLibrary import UtilitiesLibrary

testcase_utilities = UtilitiesLibrary()


class TagGeneratorTest(unittest.TestCase):
    def test_update_dictionary_by_tags(self):
        source = {'args': 'insert', 'dynamicAgentSession': 'true', 'param': {'channel': 'IB', 'custId': '[NULL]', 'ipAddress': '127.0.0.1', 'loginId': 'ibuser200', 'ssoSessionId': 'ssoSessionId'}, 'params': {'segmentId': '[REMOVE]'}, 'password': '[REMOVE]', 'realmId': '[REMOVE]', 'userId': '[REMOVE]'}
        actual = testcase_utilities.update_dictionary_by_tags(source)
        assert actual == {'args': 'insert', 'dynamicAgentSession': 'true', 'param': {'channel': 'IB', 'custId': None, 'ipAddress': '127.0.0.1', 'loginId': 'ibuser200', 'ssoSessionId': 'ssoSessionId'}, 'params': {}}

if __name__ == '__main__':
    unittest.main()
