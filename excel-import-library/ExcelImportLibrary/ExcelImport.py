from builtins import open

import io
import openpyxl
from robot.api.deco import keyword
from .ColumnData import ColumnData
from .RowData import RowData

EMPTY_VALUE: str = ""


class ExcelImport:
    """
    This is a class for reading data in the excel file. We support the excel only XLSX format.
    If you use this class, you would call the method to open the file, select the sheet name first.
    """

    def __init__(self):
        self.m_file_path = None
        self.m_workbook = None
        self.m_working_sheet = None
        self.__m_headers = []
        self.__m_test_cases = []

    @keyword("Open Excel File")
    def open_excel_file(self, file_path: str, data_only: bool = True, read_only: bool = True) -> None:
        """
        Opens the excel file from the relative path in the parameter. This is supported only XLSX file.

        :param data_only: get only value (no function)

        :param file_path: The string value that is the relative path file.
               For example c:/program file/python/lib/excel.xlsx

        :raise exception: Cannot open excel file.
        """
        try:
            if read_only:
                with open(file_path, "rb") as file_stream:
                    excel_file = io.BytesIO(file_stream.read())
                    self.m_workbook = openpyxl.load_workbook(excel_file, keep_vba=True, data_only=data_only)
                    self.m_file_path = file_path
            else:
                self.m_workbook = openpyxl.load_workbook(file_path, read_only=read_only)
                self.m_file_path = file_path
        except FileNotFoundError as exception:
            raise exception

    @keyword("Select Excel Sheet")
    def select_excel_sheet(self, sheet_name: str) -> None:
        """
        The excel must be selected the sheet name before reading the data.

        :param sheet_name: The sheet name in the excel file.
        """
        try:
            self.__clear()
            self.m_working_sheet = self.m_workbook[sheet_name]
            self.__set_headers()
        except KeyError as exception:
            raise exception

    def __set_headers(self) -> None:
        max_col = self.get_max_column()
        iter_rows = self.m_working_sheet.iter_rows(min_row=1, max_col=max_col, max_row=1, values_only=True)
        self.__m_headers = next(iter_rows)

    @keyword("Set Headers Row")
    def set_headers_row(self, headers_row=1) -> None:
        """
        Set headers row before fetching

        :param headers_row:
        """
        max_col = self.get_max_column()
        iter_rows = self.m_working_sheet.iter_rows(min_row=headers_row, max_col=max_col, max_row=headers_row,
                                                     values_only=True)
        self.__m_headers = next(iter_rows)

    @keyword("Set Headers Column")
    def set_headers_col(self, headers_col=1) -> None:
        """
        Set headers column before fetching (data transpose)

        :param headers_col:
        """
        max_row = self.get_max_row()
        iter_cols = self.m_working_sheet.iter_cols(min_col=headers_col, max_col=headers_col, max_row=max_row,
                                                     values_only=True)
        self.__m_headers = next(iter_cols)

    @keyword("Set Working Rows")
    def set_working_rows(self, start_row: int, end_row: int, max_col: int) -> None:
        """
        Limit the rows that you want to read data on the excel file by fixing the start and end row.
        The working rows maybe contain many test cases. We add the test cases into list. The test case has
        been separated by using first column in that sheet

        :param start_row: Start row is a first row of the data.

        :param end_row: End row is a last row of the data.

        :param max_col: maximun column in that sheet.
        """
        self.__m_test_cases = self.__get_rows_data(
            min_row=start_row,
            max_row=end_row,
            max_col=max_col,
            only_first_data=False
        )

    @keyword("Set Working Columns")
    def set_working_columns(self, start_col: int, end_col: int, max_row: int) -> None:
        """
        Limit the rows that you want to read data on the excel file by fixing the start and end row.
        The working rows maybe contain many test cases. We add the test cases into list. The test case has
        been separated by using first column in that sheet.

        :start_row: Start row is a first row of the data.
        :end_row: End row is a last row of the data.
        :max_col: How many column in that sheet.
        """

        self.__m_test_cases = self.__get_columns_data(
            start_col,
            end_col,
            max_row,
            False
        )

    @keyword("Get Test Case")
    def get_test_case(self, index: int) -> dict:
        """
        Gets the test case in the working row by using the index.

        :param index: The index of the test case.

        :return: A dictionary contains start row, end row, and values. The values are the dictionary that
        key and value are the header name and list of data.
        """
        try:
            return self.__format_test_case(self.__m_test_cases[index])
        except IndexError as exception:
            raise IndexError(str(exception) + ". Please set working rows first.")

    @keyword("Find Test Case")
    def find_test_case(self, sheet_name: str, test_case_name: str, headers_index=1, search_index=1, transpose=False) -> list:
        """
        Find test case by using a name of test case. The test cases maybe more than one test case then
        we add all test cases into list.

        :param sheet_name: string

        :param test_case_name: the name of the test case

        :return: test case list
        """
        if self.m_working_sheet is None or self.m_working_sheet.title != sheet_name:
            self.select_excel_sheet(sheet_name)
        if not transpose:
            self.set_headers_row(headers_index)
            focus_index_list = self.search_row(test_case_name, search_index)
        else:
            self.set_headers_col(headers_index)
            focus_index_list = self.search_column(test_case_name, search_index)
        max_row = self.get_max_row()
        max_col = self.get_max_column()
        test_case_list = []
        for focus_index in focus_index_list:
            if not transpose:
                test_case = self.__get_rows_data(min_row=focus_index, max_row=max_row, max_col=max_col, only_first_data=True)
            else:
                test_case = self.__get_columns_data(min_col=focus_index, max_col=max_col, max_row=max_row, only_first_data=True)
            test_case_list.append(self.__format_test_case(test_case[0]))
        return test_case_list

    @staticmethod
    def __format_test_case(test_case: RowData) -> dict:
        return {
            "start_row": str(test_case.get_start_row()),
            "end_row": test_case.get_end_row(),
            "values": test_case.get_columns_dict()
        }

    @keyword("Get Max Test Cases")
    def get_max_test_cases(self) -> int:
        """
        Gets maximum of test cases in the working rows.

        :return: number of max test case
        """
        return len(self.__m_test_cases)

    @keyword("Search Row")
    def search_row(self, text: str, column: int) -> list:
        """
        Search first row that contain the text.

        :param text: string text

        :param column: the column index finding

        :return: row index
        """
        text = self.__clear_text(text)
        row_index = []
        # start two for skipping header
        for row in range(2, self.get_max_row() + 1):
            value = self.__clear_text(self.get_cell(row=row, col=column))
            if value == text:
                row_index.append(row)
        return row_index

    @keyword("Search Column")
    def search_column(self, text: str, row: int) -> list:
        """
        Search first column that contain the text.

        :param text: string text

        :param row: the row index finding

        :return: column index
        """
        text = self.__clear_text(text)
        col_index = []
        for col in range(2, self.get_max_column() + 1):
            value = self.__clear_text(self.get_cell(row=row, col=col))
            if value == text:
                col_index.append(col)
        return col_index

    @staticmethod
    def __clear_text(text: str) -> str:
        if text is not None:
            return str(text).lstrip('\"').rstrip('\"').replace(" ", "").replace("\n", "").lower()
        return ""

    def __get_rows_data(self, min_row: int, max_row: int, max_col: int, only_first_data: bool) -> list:
        if self.m_working_sheet is None:
            raise SyntaxError("Please select the excel sheet before set a working rows.")
        if min_row is None or max_row is None or max_col is None:
            raise ValueError(f'min_row[{min_row}] or max_row[{max_row}] or max_col[{max_col}] should not be None.')
        headers = self.__m_headers
        working_rows = []
        index_row = min_row
        iter_rows = self.m_working_sheet.iter_rows(
            min_row=index_row,
            max_row=max_row,
            max_col=max_col,
            values_only=True
        )
        for row in iter_rows:
            if row[0] is not None:
                if index_row == 1:
                    headers = self.__get_header(transpose=False)
                else:
                    if only_first_data and len(working_rows) >= 1:
                        break
                    working_rows.append(self.__get_row(row, headers, index_row, max_col))
            else:
                self.__add_next_row(
                    previous_row_data=working_rows[len(working_rows) - 1],
                    row=row,
                    max_col=max_col
                )
            index_row += 1
        return working_rows

    def __get_columns_data(self, min_col: int, max_col: int, max_row: int, only_first_data: bool) -> list:
        if self.m_working_sheet is None:
            raise SyntaxError("Please select the excel sheet before set a working rows.")
        if min_col is None or max_col is None or max_row is None:
            raise ValueError(f'min_row[{min_col}] or max_row[{max_col}] or max_col[{max_row}] should not be None.')
        headers = self.__m_headers
        working_cols = []
        index_col = min_col
        iter_cols = self.m_working_sheet.iter_cols(
            min_col=min_col,
            max_col=max_col,
            max_row=max_row,
            values_only=True
        )
        for col in iter_cols:
            if col[0] is not None:
                if index_col == 1:
                    headers = self.__get_header(transpose=True)
                else:
                    if only_first_data and len(working_cols) >= 1:
                        break
                    working_cols.append(self.__get_col(col, headers, index_col, max_row))
            else:
                self.__add_next_col(
                    previous_col_data=working_cols[len(working_cols)-1],
                    col=col,
                    max_row=max_row
                )
            index_col += 1
        return working_cols

    def __get_header(self, transpose=False):
        if transpose:
            max_row = self.get_max_row()
            return next(self.m_working_sheet.iter_cols(
                min_col=1,
                max_row=max_row,
                max_col=1,
                values_only=True
            ))
        else:
            max_col = self.get_max_column()
            return next(self.m_working_sheet.iter_rows(
                min_row=1,
                max_col=max_col,
                max_row=1,
                values_only=True
            ))

    @keyword("Get Cell")
    def get_cell(self, row: int, col: int) -> str:
        """
        Gets a data in the row and col.

        :param row: index of the row

        :param col: index of the column

        :return: data in cell
        """
        try:
            return self.m_working_sheet.cell(row, col).value
        except AttributeError as exception:
            self.__throw_attribute_error(exception)

    @keyword("Get Max Row")
    def get_max_row(self) -> int:
        """
        Gets maximum of the row in that sheet.

        :return: number of max row
        """
        try:
            return self.m_working_sheet.max_row
        except AttributeError as exception:
            self.__throw_attribute_error(exception)

    @keyword("Get Max Column")
    def get_max_column(self) -> int:
        """
        Gets maximum of the column in that sheet.

        :return: number of max column
        """
        try:
            return self.m_working_sheet.max_column
        except AttributeError as exception:
            self.__throw_attribute_error(exception)

    def __throw_attribute_error(self, exception):
        raise AttributeError(str(exception) + ". Please select the excel sheet before set a working rows.")

    def __clear(self) -> None:
        self.m_working_sheet = None
        self.__m_headers = []
        self.__m_test_cases = []

    @staticmethod
    def __get_row(row, headers, index_row: int, max_col: int):
        row_data = RowData(index_row)
        for index in range(0, max_col):
            column_data = ColumnData()
            if headers:
                column_data.set_header(headers[index])
            column_data.add_value(row[index])
            row_data.add_column(column_data)
        return row_data

    @staticmethod
    def __get_col(col, headers, index_col: int, max_row: int):
        col_data = RowData(index_col)
        for index in range(0, max_row):
            column_data = ColumnData()
            if headers:
                column_data.set_header(headers[index])
            column_data.add_value(col[index])
            col_data.add_column(column_data)
        return col_data

    @staticmethod
    def __add_next_row(previous_row_data, row, max_col):
        previous_row_data.increase_row()
        for index in range(0, max_col):
            column_data = previous_row_data.get_columns()[index]
            value = row[index]
            if value is not None:
                column_data.add_value(value)
            else:
                column_data.add_value(EMPTY_VALUE)

    @staticmethod
    def __add_next_col(previous_col_data, col, max_row):
        previous_col_data.increase_row()
        for index in range(0, max_row):
            row_data = previous_col_data.get_columns()[index]
            value = col[index]
            if value is not None:
                row_data.add_value(value)
            else:
                row_data.add_value(EMPTY_VALUE)

    @keyword("To List")
    def to_list(self, text: str, separator=",") -> list:
        """
        Convert string (string like list) to list

        :param text:

        :param separator:

        :return: list
        """
        text_list = []
        if text is not None:
            for t in text.strip("\n").split(separator):
                text_list.append(t.strip())
        return text_list

    @keyword("Get Sheet Names")
    def get_sheet_names(self) -> list:
        """
        Get current sheet names in excel file

        :return: list of sheet names
        """
        return self.m_workbook.sheetnames
