import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from UtilitiesLibrary import UtilitiesLibrary

testcase_utilities = UtilitiesLibrary()

class SocketManageMentTest(unittest.TestCase):
    def test_encrypt_sha256(self):
        result = testcase_utilities.encrypt_sha256('hello there')
        expect = "b'EpmMAXBm6w0qcLlObtMZKYWFXOOQ8yG724MgIoiL0lE='"
        str_result = str(result)
        assert str_result == expect

    def test_send_message_socket(self):
        result = testcase_utilities.send_message_socket('192.168.1.1', 80, 'AvKFM4YK02YwMUsxRTlL')
        print(result)

    def test_update_message_socket(self):
        result = testcase_utilities.update_message_socket('AvKFM4YK02YwMUsxRTlL', 'Hello', 2, 10)
        expect = "b'AvJIZWxsbyAgICAgRTlL'"
        str_result = str(result)
        assert str_result == expect

if __name__ == '__main__':
    unittest.main()