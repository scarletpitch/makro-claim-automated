from robot.api.deco import keyword
from robot.api import logger

class ExcelUpdate:

    @keyword("Check Sheet Existed")
    def check_sheet_existed(self, sheet_name):
        """
        Check sheet exist or not

        :param sheet_name:

        :return: bool
        """
        try:
            ws = self.m_workbook[sheet_name]  # try to access a non-existent worksheet
            return True
        except Exception:
            return False

    @keyword("Remove Existed Sheet")
    def remove_existed_sheet(self, sheet_name):
        """
        Remove existed sheet

        :param sheet_name:

        :return: bool
        """
        logger.console(f'{sheet_name} removing...')
        try:
            std = self.m_workbook.get_sheet_by_name(sheet_name)
            self.m_workbook.remove_sheet(std)
            self.m_workbook.save(self.m_file_path)
            return True
        except Exception:
            return False

    @keyword("Clone Sheet")
    def clone_sheet(self, source_name: str, dest_name: str, clone_row: int = -1, clone_col: int = -1):
        """
        Clone test data sheet. Can select row and column that need to clone.

        :param source_name: existed source sheet name

        :param dest_name: existed clone destination sheet name

        :param clone_row: clone row

        :param clone_col: clone column
        """
        logger.console(f'sheet cloning from {source_name} to {dest_name}...')
        self.select_excel_sheet(source_name)
        dest_sheet = self.m_workbook.copy_worksheet(self.m_working_sheet)
        dest_sheet.title = dest_name
        max_col = self.get_max_column()
        max_row = self.get_max_row()
        logger.console(f'max_row: {max_row}')
        logger.console(f'max_col: {max_col}')
        if clone_row > -1:
            dest_sheet.delete_rows(clone_row+1, max_row)
        if clone_col > -1:
            dest_sheet.delete_cols(clone_col+1, max_col)
        self.m_workbook.save(self.m_file_path)

    @keyword("Update Test Result")
    def update_test_result(self, sheet_name: str, row: int, col: int, value):
        """
        Update test result into sheet (insert value to excel)

        :param sheet_name:

        :param row:

        :param col:

        :param value:
        """
        self.select_excel_sheet(sheet_name)
        self.m_working_sheet.cell(row, col).value = value
        self.m_workbook.save(self.m_file_path)

    @keyword("Excel Close")
    def excel_close(self):
        """
        close excel
        """
        self.m_workbook.close()