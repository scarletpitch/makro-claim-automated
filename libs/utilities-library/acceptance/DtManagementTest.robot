*** Settings ***
Library     UtilitiesLibrary

*** Test Cases ***
test_get_now_datetime
    [Tags]      utilities-library    dt_management_keywords   test13
    get_now_datetime_keywords

test_get_now_datetime_iso
    [Tags]      utilities-library    dt_management_keywords   test14
    get_now_datetime_iso_keywords

test_get_now_total_seconds
    [Tags]      utilities-library    dt_management_keywords   test15
    get_now_total_seconds_keywords

test_get_current_date_with_local_timezone
    [Tags]      utilities-library    dt_management_keywords   test16
    get_current_date_with_local_timezone_keywords

test_convert_epoch_to_date_and_time
    [Tags]      utilities-library    dt_management_keywords   test17
    convert_epoch_to_date_and_time_keywords

test_get_iso_datetime_tzcus
    [Tags]      utilities-library    dt_management_keywords   test18
    get_iso_datetime_tzcus_keywords

test_get_utc_datetime
    [Tags]      utilities-library    dt_management_keywords   test19
    get_utc_datetime_keywords

test_get_iso_datetime_ml
    [Tags]      utilities-library    dt_management_keywords   test20
    get_iso_datetime_ml_keywords

*** Keywords ***
get_now_datetime_keywords
    ${result} =      Get Now UTC Datetime
    log     ${result}

get_now_datetime_iso_keywords
    ${result} =      Get Now ISO Datetime
    log     ${result}

get_now_total_seconds_keywords
    ${result} =      Get Now Total Seconds
    log     ${result}

get_current_date_with_local_timezone_keywords
    ${result} =      Get Current Date With Local Timezone
    log     ${result}

convert_epoch_to_date_and_time_keywords
    ${data} =   convert to integer    1575339570
    ${result} =      Convert Epoch To Datetime      ${data}
    log     ${result}

get_iso_datetime_tzcus_keywords
    ${result} =      Get ISO_DATETIME_TZCUS
    log     ${result}

get_utc_datetime_keywords
    ${result} =      Get UTC Datetime
    log     ${result}

get_iso_datetime_ml_keywords
    ${result} =      Get ISO_DATETIME_ML
    log     ${result}