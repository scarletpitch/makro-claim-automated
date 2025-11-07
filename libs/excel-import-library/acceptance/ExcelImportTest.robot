*** Settings ***
Library    ExcelImportLibrary

*** Test Cases ***
test_open_excel_file
    [Tags]      test_excel_import_library    excel_import_test   test1
    test_open_excel_file_keywords

test_select_excel_sheet
    [Tags]      test_excel_import_library    excel_import_test   test2
    test_select_excel_sheet_keywords

test_set_headers_row
    [Tags]      test_excel_import_library    excel_import_test   test3
    test_set_headers_row_keywords

test_set_working_rows
    [Tags]      test_excel_import_library    excel_import_test   test4
    test_set_working_rows_keywords

test_set_headers_column
    [Tags]      test_excel_import_library    excel_import_test   test5
    test_set_headers_column_keywords

test_set_working_columns
    [Tags]      test_excel_import_library    excel_import_test   test6
    test_set_working_columns_keywords

test_get_test_case
    [Tags]      test_excel_import_library    excel_import_test   test7
    test_get_test_case_keywords

test_find_test_case
    [Tags]      test_excel_import_library    excel_import_test   test8
    test_find_test_case_keywords

test_get_max_test_cases
    [Tags]      test_excel_import_library    excel_import_test   test9
    test_get_max_test_cases_keywords

test_search_row
    [Tags]      test_excel_import_library    excel_import_test   test10
    test_search_row_keywords

test_get_cell
    [Tags]      test_excel_import_library    excel_import_test   test11
    test_get_cell_keywords

test_get_max_row
    [Tags]      test_excel_import_library    excel_import_test   test12
    test_get_max_row_keywords

test_get_max_column
    [Tags]      test_excel_import_library    excel_import_test   test13
    test_get_max_column_keywords

test_to_list
    [Tags]      test_excel_import_library    excel_import_test   test14
    test_to_list_keywords

test_get_sheet_names
    [Tags]      test_excel_import_library    excel_import_test   test15
    test_get_sheet_names_keywords

*** Keywords ***
test_open_excel_file_keywords
    ${result} =     Open Excel File         ${EXECDIR}${/}excel.xlsx
    run keyword if    ${result}==${None}    log    test_open_excel_file_keywords : Success
    ...    ELSE    fail    test_open_excel_file_keywords : Fail

test_select_excel_sheet_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    ${result} =     Select Excel Sheet      main
    run keyword if    ${result}==${None}    log    test_select_excel_sheet_keywords : Success
    ...    ELSE    fail    test_select_excel_sheet_keywords : Fail

test_set_headers_row_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    ${result} =     Set Headers Row
    run keyword if    ${result}==${None}    log    test_set_headers_row_keywords : Success
    ...    ELSE    fail    test_set_headers_row_keywords : Fail

test_set_working_rows_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Row
    ${result} =     Set Working Rows    1   20  4
    run keyword if    ${result}==${None}    log    test_set_working_rows_keywords : Success
    ...    ELSE    fail    test_set_working_rows_keywords : Fail

test_set_headers_column_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    ${result} =     Set Headers Column
    run keyword if    ${result}==${None}    log    test_set_headers_column_keywords : Success
    ...    ELSE    fail    test_set_headers_column_keywords : Fail

test_set_working_columns_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    ${result} =     Set Working Columns         2   4   20
    run keyword if    ${result}==${None}    log    test_set_working_columns_keywords : Success
    ...    ELSE    fail    test_set_working_columns_keywords : Fail

test_get_test_case_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         2   2   1
    ${result} =     Get Test Case     0
    set test variable    ${expect}    {'start_row': '2', 'end_row': 2, 'values': {'Test ID': ['TEST_001']}}
    run keyword if    ${result}==${expect}    log    test_get_test_case_keywords : Success
    ...    ELSE    fail    test_get_test_case_keywords : Fail

test_find_test_case_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Find Test Case      results    สร้าง Prospect for app บุคคลธรรมดา (V1)   headers_index=1     search_index=2  transpose=${TRUE}
    ${result} =     convert to string    ${result}
    set test variable    ${expect}    [{'start_row': '2', 'end_row': 2, 'values': {'Test ID': ['TEST_001'], 'Test Case': ['สร้าง Prospect for app บุคคลธรรมดา (V1)'], 'Description': ['-'], 'Tag': ['PROSPECT'], 'Individual.CIS_ID': ['29649802'], 'Organize.CIS_ID': [None]}}]
    run keyword if    ${result}==${expect}    log    test_find_test_case_keywords : Success
    ...    ELSE    fail    test_find_test_case_keywords : Fail

test_get_max_test_cases_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Get Max Test Cases
    set test variable    ${expect}    1
    run keyword if    ${result}==${expect}    log    test_get_max_test_cases_keywords : Success
    ...    ELSE    fail    test_get_max_test_cases_keywords : Fail

test_search_row_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Search Row      กมล    2
    set test variable    ${expect}    [14]
    run keyword if    ${result}==${expect}    log    test_search_row_keywords : Success
    ...    ELSE    fail    test_search_row_keywords : Fail

test_search_column_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Search Column      กมล    14
    set test variable    ${expect}    [2]
    run keyword if    ${result}==${expect}    log    test_search_column_keywords : Success
    ...    ELSE    fail    test_search_column_keywords : Fail

test_get_cell_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Get Cell      1    2
    set test variable    ${expect}    TEST_001
    run keyword if    '${result}==${expect}'    log    test_get_cell_keywords : Success
    ...    ELSE    fail    test_get_cell_keywords : Fail

test_get_max_row_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Get Max Row
    set test variable    ${expect}    20
    run keyword if    ${result}==${expect}    log    test_get_max_row_keywords : Success
    ...    ELSE    fail    test_get_max_row_keywords : Fail

test_get_max_column_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Get Max Column
    set test variable    ${expect}    2
    run keyword if    ${result}==${expect}    log    test_get_max_column_keywords : Success
    ...    ELSE    fail    test_get_max_column_keywords : Fail

test_to_list_keywords
    ${result} =     To List     a1,a2,a3,a4
    ${expect} =  set variable   ['a1', 'a2', 'a3', 'a4']
    run keyword if    ${result}==${expect}    log    test_to_list_keywords : Success
    ...    ELSE    fail    test_to_list_keywords : Fail

test_get_sheet_names_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns         1   2   20
    ${result} =     Get Sheet Names
    ${result} =     convert to string    ${result}
    set test variable    ${expect}    ['setting', 'endpoint_list', 'main', 'results']
    run keyword if    ${result}==${expect}    log    test_get_sheet_names_keywords : Success
    ...    ELSE    fail    test_get_sheet_names_keywords : Fail