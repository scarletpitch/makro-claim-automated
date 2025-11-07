*** Settings ***
Library     UtilitiesLibrary
Library     Collections

*** Test Cases ***
test_verify_response_body
    [Tags]      utilities-library    dict_management_keywords   test1
    verify_response_body_keywords

test_update_data_into_original_dictionary
    [Tags]      utilities-library    dict_management_keywords   test2
    update_data_into_original_dictionary_keywords

test_convert_suds_object_to_dict
    [Tags]      utilities-library    dict_management_keywords   test3
    convert_suds_object_to_dict_keywords

test_update_the_value_for_the_key_list
    [Tags]      utilities-library    dict_management_keywords   test4
    update_the_value_for_the_key_list_keywords

test_update_the_value_for_selected_key
    [Tags]      utilities-library    dict_management_keywords   test5
    update_the_value_for_selected_key_keywords

test_get_the_value_for_selected_key
    [Tags]      utilities-library    dict_management_keywords   test6
    get_the_value_for_selected_key_keywords

test_get_list_diffs
    [Tags]      utilities-library    dict_management_keywords   test7
    get_list_diffs_keywords

test_delete_key_in_dictionary
    [Tags]      utilities-library    dict_management_keywords   test8
    delete_key_in_dictionary_keywords

test_update_value_from_original_dictionary
    [Tags]      utilities-library    dict_management_keywords   test9
    update_value_from_original_dictionary_keywords

test_update_the_value_for_the_key_list_to_decimal
    [Tags]      utilities-library    dict_management_keywords   test10
    update_the_value_for_the_key_list_to_decimal_keywords

test_update_the_value_for_selected_key_to_decimal
    [Tags]      utilities-library    dict_management_keywords   test11
    update_the_value_for_selected_key_to_decimal_keywords

test_validate_response_body
    [Tags]      utilities-library    dict_management_keywords   test12
    validate_response_body_keywords

*** Keywords ***
verify_response_body_keywords
    ${actual} =      set variable    {'data': 'Update All Resource', 'message': 'Function Put'}
    ${expect} =      set variable    {'data': 'Update All Resource', 'message': 'Function Put'}
    ${result} =      Verify Response Body      ${actual}     ${expect}

update_data_into_original_dictionary_keywords
    &{source} =   Create Dictionary		hello=to_override
    &{overrides} =   Create Dictionary		hello=over
    ${expect} =      set variable    {'hello': 'over'}
    ${result} =      Update Data Into Original Dictionary      ${source}     ${overrides}
    run keyword if    ${result}==${expect}    log    test_update_data_into_original_dictionary_keywords : Success
    ...    ELSE    fail    test_update_data_into_original_dictionary_keywords : Fail

convert_suds_object_to_dict_keywords
    ${source} =      set variable    {'hello': 'to_override'}
    ${expect} =      set variable    {'hello': 'to_override'}
    ${result} =      Convert Subs Object to Dictionary      ${source}
    run keyword if    ${result}==${expect}    log    test_update_data_into_original_dictionary_keywords : Success
    ...    ELSE    fail    test_update_data_into_original_dictionary_keywords : Fail

update_the_value_for_the_key_list_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=null   transactionAmt=null
    ${key} =        Create list    accName
    ${value} =      set variable   H
    ${expect} =     set variable   {'funcName': 'API123', 'appId': '222', 'accName': 'H', 'accNumber': '123456', 'accAmount': 'null', 'transactionAmt': 'null'}
    ${result} =     Update The Value For The Key List      ${source}    ${key}  ${value}
    run keyword if    ${result}==${expect}    log    test_update_the_value_for_the_key_list_keywords : Success
    ...    ELSE    fail    test_update_the_value_for_the_key_list_keywords : Fail

update_the_value_for_selected_key_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=null   transactionAmt=null
    ${key} =        set variable    accName
    ${value} =      set variable   12345
    ${expect} =     set variable   {'funcName': 'API123', 'appId': '222', 'accName': '12345', 'accNumber': '123456', 'accAmount': 'null', 'transactionAmt': 'null'}
    ${result} =     Update The Value For Selected Key      ${source}    ${key}  ${value}
    run keyword if    ${result}==${expect}    log    test_update_the_value_for_selected_key : Success
    ...    ELSE    fail    test_update_the_value_for_selected_key : Fail

get_the_value_for_selected_key_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=null   transactionAmt=null
    ${key} =        set variable    accName
    ${expect} =     set variable   KBANK
    ${result} =     Get The Value For Selected Key      ${source}    ${key}
    run keyword if    '${result}'=='${expect}'    log    test_get_the_value_for_selected_key : Success
    ...    ELSE    fail    test_get_the_value_for_selected_key : Fail

get_list_diffs_keywords
    ${source1} =    Create list    10   15  20  25  30  35  40
    ${source2} =    Create list    20   40  35
    ${expect} =     Create list    10   15  25  30
    ${result} =     Get List Diffs      ${source1}    ${source2}
    run keyword if    ${result}==${expect}    log    test_get_list_diffs : Success
    ...    ELSE    fail    test_get_list_diffs : Fail

delete_key_in_dictionary_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=null   transactionAmt=null
    ${key} =    set variable    accNumber
    ${expect} =     set variable    {'funcName': 'API123', 'appId': '222', 'accName': 'KBANK', 'accAmount': 'null', 'transactionAmt': 'null'}
    ${result} =     Delete Key In Dictionary      ${source}    ${key}
    run keyword if    ${result}==${expect}    log    test_delete_key_in_dictionary : Success
    ...    ELSE    fail    test_delete_key_in_dictionary : Fail

update_value_from_original_dictionary_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=null   transactionAmt=null
    ${target} =   Create Dictionary		appId=None   accName=None
    ${expect} =     set variable    {'appId': '222', 'accName': 'KBANK'}
    ${result} =     Update Value From Original Dictionary      ${source}    ${target}
    run keyword if    ${result}==${expect}    log    test_update_value_from_original_dictionary : Success
    ...    ELSE    fail    test_update_value_from_original_dictionary : Fail

update_the_value_for_the_key_list_to_decimal_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=1,234   transactionAmt=3.14
    ${key} =   Create list		accAmount   amtTranfer
    ${result} =     Update The Value For The Key List To Decimal      ${source}    ${key}
    log    ${result}

update_the_value_for_selected_key_to_decimal_keywords
    ${source} =   Create Dictionary		funcName=API123     appId=222   accName=KBANK   accNumber=123456   accAmount=1,234   transactionAmt=null
    ${target} =   set variable		accAmount
    ${result} =     Update The Value For Selected Key List To Decimal      ${source}    ${target}
    log    ${result}

validate_response_body_keywords
    ${actual} =      set variable    {'data': 'Update All Resource', 'message': 'Function Put'}
    ${expect} =      set variable    {'data': 'Update All Resource', 'message': 'Function Put'}
    ${result} =      Verify Response Body      ${actual}     ${expect}
