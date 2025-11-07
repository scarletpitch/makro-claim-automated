*** Settings ***
Library    SeleniumLibrary
Library    ../resources/browser_setup.py
Test Template    Login Test Template

*** Variables ***
${URL}         https://transferhub-uat.cpaxtra.co.th/index.html
${PASSWORD}    Qa@12345
# ${CHROMEDRIVER_PATH}    /Users/pisha/.wdm/drivers/chromedriver/mac64/142.0.7444.61/chromedriver-mac-arm64/chromedriver

*** Test Cases ***
QA_SGR1    QA_SGR1
QA_SGR3    QA_SGR3

*** Keywords ***
Login Test Template
    [Arguments]    ${username}
    ${CHROMEDRIVER_PATH}=    Get Chromedriver Path
    Open Browser    ${URL}    chrome    executable_path=${CHROMEDRIVER_PATH}
    Wait Until Page Contains Element    xpath=//a[@class='mx-name-tabPage1' and normalize-space()='Local']    10s
    Click Element    xpath=//a[@class='mx-name-tabPage1' and normalize-space()='Local']
    Wait Until Page Contains Element    xpath=//input[contains(@placeholder, 'Username')]    10s
    Input Text    xpath=//input[@placeholder='Username']    ${username}
    Input Text    xpath=//input[@placeholder='Password']    ${PASSWORD}
    Click Button    xpath=//button[contains(@class, 'mx-name-signInButton1') and normalize-space()='Log in']
    Wait Until Page Contains Element    xpath=//span[contains(text(), 'DC-Store Makro Claim')]    timeout=5s
    Capture Page Screenshot
    Close Browser
