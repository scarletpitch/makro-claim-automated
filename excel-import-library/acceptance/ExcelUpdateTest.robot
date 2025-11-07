*** Settings ***
Library    ExcelImportLibrary

*** Test Cases ***
test_check_sheet_existed
    [Tags]      test_excel_import_library    excel_update_test   test16
    test_check_sheet_existed_keywords

test_clone_sheet
    [Tags]      test_excel_import_library    excel_update_test   test17
    test_clone_sheet_keywords

test_remove_existed_sheet
    [Tags]      test_excel_import_library    excel_update_test   test18
    test_remove_existed_sheet_keywords

test_update_test_result
    [Tags]      test_excel_import_library    excel_update_test   test19
    test_update_test_result_keywords

*** Keywords ***
test_check_sheet_existed_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx
    Select Excel Sheet      main
    Set Headers Column
    Set Working Columns     1   2   20
    ${result} =    Check Sheet Existed     main
    ${expect}   set variable    ${TRUE}
    run keyword if    ${result}==${expect}    log    test_check_sheet_existed_keywords : Success
    ...    ELSE    fail    test_check_sheet_existed_keywords : Fail

test_clone_sheet_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx       read_only=${FALSE}
    Clone Sheet     setting    setting123
    ${result} =   Get Sheet Names
    ${count} =    Get length    ${result}
    set test variable    ${actual}    ${result}[${count-1}]
    set test variable    ${expect}    setting123
    run keyword if    '${actual}'=='${expect}'    log    test_clone_sheet_keywords : Success
    ...    ELSE    fail    test_clone_sheet_keywords : Fail
    [Teardown]    Remove Existed Sheet     setting123

test_remove_existed_sheet_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx       read_only=${FALSE}
    Clone Sheet     setting    setting123
    Remove Existed Sheet     setting123
    ${result} =   Get Sheet Names
    log    ${result}
    ${count} =    Get length    ${result}
    set test variable    ${actual}    ${result}[${count-1}]
    set test variable    ${expect}    results
    run keyword if    '${actual}'=='${expect}'    log    test_remove_existed_sheet_keywords : Success
    ...    ELSE    fail    test_remove_existed_sheet_keywords : Fail

test_update_test_result_keywords
    Open Excel File         ${EXECDIR}${/}excel.xlsx       read_only=${FALSE}
    ${result} =     Update Test Result     setting      7       2       Hello
    run keyword if    ${result}==${None}    log    test_update_test_result_keywords : Success
    ...    ELSE    fail    test_update_test_result_keywords : Fail