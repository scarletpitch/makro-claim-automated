from .ExcelImport import ExcelImport
# from ColumnData import ColumnData
# from RowData import RowData
from .ExcelUpdate import ExcelUpdate
from .__version__ import VERSION

__version__ = VERSION


class ExcelImportLibrary(ExcelImport, ExcelUpdate):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__
