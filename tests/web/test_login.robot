*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google And Search
    Open Browser    https://google.com    chrome
    Input Text    name=q    Robot Framework
    Press Keys    name=q    RETURN
    Page Should Contain    Robot Framework
    Close Browser
