*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/common_variables.robot

*** Keywords ***
Open Login Page
    Open Browser        
    Maximize Browser Window

Input Credentials
    Input Text    id=username    
    Input Text    id=password    

Submit Login
    Click Button    id=login-button

Login Should Be Successful
    Page Should Contain    Welcome

Login To Application
    [Documentation]    Reusable login keyword
    Open Login Page
    Input Credentials
    Submit Login
    Login Should Be Successful
