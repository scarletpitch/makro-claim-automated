*** Settings ***
Library     UtilitiesLibrary

*** Test Cases ***
test_update_dictionary_by_tags
    [Tags]      utilities-library    tag_generator_keywords   test24
    update_dictionary_by_tags_keywords

*** Keywords ***
update_dictionary_by_tags_keywords
    ${source} =     set variable    {'args': 'insert', 'dynamicAgentSession': 'true'}
    ${expect} =     set variable    {'args': 'insert', 'dynamicAgentSession': 'true'}
    ${result} =      Update Dictionary By Tags     ${source}
    run keyword if    ${result}==${expect}    log    test_encrypt_sha256 : Success
    ...    ELSE    fail    test_encrypt_sha256 : Fail