*** Settings ***
Library     UtilitiesLibrary

*** Test Cases ***
test_encrypt_sha256
    [Tags]      utilities-library    socket_management_keywords   test21
    encrypt_sha256_keywords

test_send_message_socket
    [Tags]      utilities-library    socket_management_keywords   test22
    send_message_socket_keywords

test_update_message_socket
    [Tags]      utilities-library    socket_management_keywords   test23
    update_message_socket_keywords

*** Keywords ***
encrypt_sha256_keywords
    ${expect} =     set variable    EpmMAXBm6w0qcLlObtMZKYWFXOOQ8yG724MgIoiL0lE=
    ${result} =      Encrypt Sha256     hello there
    run keyword if    '${result}'=='${expect}'    log    test_encrypt_sha256 : Success
    ...    ELSE    fail    test_encrypt_sha256 : Fail
    log     ${result}

send_message_socket_keywords
    ${result} =      Send Message Socket    192.168.1.1     80      AvKFM4YK02YwMUsxRTlL
    log     ${result}

update_message_socket_keywords
    ${expect} =     set variable    AvJIZWxsbyAgICAgRTlL
    ${result} =      Update Message Socket      AvKFM4YK02YwMUsxRTlL    Hello   2   10
    run keyword if    '${result}'=='${expect}'    log    test_update_message_socket : Success
    ...    ELSE    fail    test_update_message_socket : Fail
    log     ${result}