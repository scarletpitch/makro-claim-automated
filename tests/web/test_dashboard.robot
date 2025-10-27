*** Settings ***
Resource   ../../resources/keywords/login_keywords.robot
Resource   ../../resources/keywords/dashboard_keywords.robot

*** Test Cases ***
User Can Access Dashboard
    Login To Application
    Go To Dashboard
    [Teardown]    Close Browser
