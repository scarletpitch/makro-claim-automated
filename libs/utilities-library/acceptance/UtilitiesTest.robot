*** Settings ***
Library     UtilitiesLibrary

*** Test Cases ***
test_verify_text_with_regEx
    [Tags]      utilities-library    utilitieskeywords   test25
    verify_text_with_regEx_keywords

test_generate_request_uid
    [Tags]      utilities-library    utilitieskeywords   test26
    generate_request_uid_keywords

*** Variables ***
&{expact_data}           data=Create Resource       message=Function Post
&{header_test}           Accept-Encoding=identity

*** Keywords ***
verify_text_with_regEx_keywords
    ${result} =     Verify Text With RegEx      test123     test123
    ${expect} =    set variable    ${True}
    run keyword if    ${result}==${expect}    log    test_verify_text_with_regEx_keywords : Success
    ...    ELSE    fail    test_verify_text_with_regEx_keywords : Fail

generate_request_uid_keywords
    ${result} =     Generate Request UID      test
    log    ${result}