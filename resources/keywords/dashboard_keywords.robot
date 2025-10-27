*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Go To Dashboard
    Click Link    xpath=//a[text()="Dashboard"]
    Page Should Contain    Dashboard Overview
