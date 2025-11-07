import unittest
import sys
import os
tests_d = os.path.dirname(os.path.realpath(__file__))
src_d = os.path.abspath(os.path.join(tests_d, '..', ''))
sys.path.insert(1, src_d)
from ExcelImportLibrary import ExcelImportLibrary

testcase_excel = ExcelImportLibrary()
tests_path = os.getcwd()
path_excel = tests_path+"/excel.xlsx"

class ExcelUpdateTest(unittest.TestCase):
    def test_check_sheet_existed(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.check_sheet_existed('main')
        expect = True
        assert result == expect

    def test_clone_sheet(self):
        testcase_excel.open_excel_file(path_excel,read_only=False)
        testcase_excel.clone_sheet('setting','setting123')
        result = testcase_excel.get_sheet_names()
        count = len(result)
        actual = result[count-1]
        expect = "setting123"
        testcase_excel.remove_existed_sheet('setting123')
        assert actual == expect

    def test_remove_existed_sheet(self):
        testcase_excel.open_excel_file(path_excel, read_only=False)
        testcase_excel.clone_sheet('setting', 'setting123')
        testcase_excel.remove_existed_sheet('setting123')
        result = testcase_excel.get_sheet_names()
        count = len(result)
        actual = result[count - 1]
        expect = "results"
        assert actual == expect

    def test_update_test_result(self):
        testcase_excel.open_excel_file(path_excel, read_only=False)
        result = testcase_excel.update_test_result('setting', 7, 2, 'Hello')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()