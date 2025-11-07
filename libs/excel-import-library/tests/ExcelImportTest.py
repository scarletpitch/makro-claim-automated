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

class ExcelImportTest(unittest.TestCase):
    def test_open_excel_file(self):
        result = testcase_excel.open_excel_file(path_excel)
        self.assertIsNone(result)

    def test_select_excel_sheet(self):
        testcase_excel.open_excel_file(path_excel)
        result = testcase_excel.select_excel_sheet('main')
        self.assertIsNone(result)

    def test_set_headers_row(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        result = testcase_excel.set_headers_row()
        self.assertIsNone(result)

    def test_set_working_rows(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_row()
        result = testcase_excel.set_working_rows(1,20,4)
        self.assertIsNone(result)

    def test_set_headers_column(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        result = testcase_excel.set_headers_col()
        self.assertIsNone(result)

    def test_set_working_columns(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        result = testcase_excel.set_working_columns(2,4,20)
        self.assertIsNone(result)

    def test_get_test_case(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(2, 2, 1)
        result = testcase_excel.get_test_case(0)
        expect = {'start_row': '2', 'end_row': 2, 'values': {'Test ID': ['TEST_001']}}
        assert result == expect

    def test_find_test_case(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.find_test_case('results', 'สร้าง Prospect for app บุคคลธรรมดา (V1)', headers_index=1,search_index=2, transpose=True)
        expect = [{'start_row': '2', 'end_row': 2, 'values': {'Test ID': ['TEST_001'], 'Test Case': ['สร้าง Prospect for app บุคคลธรรมดา (V1)'], 'Description': ['-'], 'Tag': ['PROSPECT'], 'Individual.CIS_ID': ['29649802'], 'Organize.CIS_ID': [None]}}]
        assert result == expect

    def test_get_max_test_cases(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.get_max_test_cases()
        expect = 1
        assert result == expect

    def test_search_row(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.search_row('กมล',2)
        expect = [14]
        assert result == expect

    def test_search_column(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.search_column('กมล',14)
        expect = [2]
        assert result == expect

    def test_get_cell(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.get_cell(1,2)
        expect = 'TEST_001'
        assert result == expect

    def test_get_max_row(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.get_max_row()
        expect = 20
        assert result == expect

    def test_get_max_column(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.get_max_column()
        expect = 2
        assert result == expect

    def test_to_list(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.to_list('b1,b2,b3,b4')
        expect = ['b1', 'b2', 'b3', 'b4']
        assert result == expect

    def test_get_sheet_names(self):
        testcase_excel.open_excel_file(path_excel)
        testcase_excel.select_excel_sheet('main')
        testcase_excel.set_headers_col()
        testcase_excel.set_working_columns(1, 2, 20)
        result = testcase_excel.get_sheet_names()
        expect = ['setting', 'endpoint_list', 'main', 'results']
        assert result == expect

if __name__ == '__main__':
    unittest.main()