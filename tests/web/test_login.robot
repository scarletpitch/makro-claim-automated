*** Settings ***
Resource   ../../resources/keywords/login_keywords.robot

*** Test Cases ***
User Can Login Successfully
    Login To Application
    [Teardown]    Close Browser
