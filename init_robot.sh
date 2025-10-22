#!/bin/bash
echo "🚀 Initializing Robot Framework project..."

# Create folder structure
mkdir -p tests/web tests/api resources/keywords resources/variables results

# Create requirements
cat > requirements.txt <<EOF
robotframework
robotframework-seleniumlibrary
robotframework-requests
EOF

# Create variables file
cat > resources/variables/common_variables.robot <<EOF
*** Variables ***
${BASE_URL}       https://example.com
${LOGIN_URL}      ${BASE_URL}/login
${USERNAME}       testuser
${PASSWORD}       123456
${BROWSER}        chrome
EOF

# Create reusable keyword file for login
cat > resources/keywords/login_keywords.robot <<EOF
*** Settings ***
Library    SeleniumLibrary
Resource   ../variables/common_variables.robot

*** Keywords ***
Open Login Page
    Open Browser    ${LOGIN_URL}    ${BROWSER}
    Maximize Browser Window

Input Credentials
    Input Text    id=username    ${USERNAME}
    Input Text    id=password    ${PASSWORD}

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
EOF

# Example keyword for dashboard
cat > resources/keywords/dashboard_keywords.robot <<EOF
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Go To Dashboard
    Click Link    xpath=//a[text()="Dashboard"]
    Page Should Contain    Dashboard Overview
EOF

# Example test for login
cat > tests/web/test_login.robot <<EOF
*** Settings ***
Resource   ../../resources/keywords/login_keywords.robot

*** Test Cases ***
User Can Login Successfully
    Login To Application
    [Teardown]    Close Browser
EOF

# Example test for dashboard
cat > tests/web/test_dashboard.robot <<EOF
*** Settings ***
Resource   ../../resources/keywords/login_keywords.robot
Resource   ../../resources/keywords/dashboard_keywords.robot

*** Test Cases ***
User Can Access Dashboard
    Login To Application
    Go To Dashboard
    [Teardown]    Close Browser
EOF

# Example API test
cat > tests/api/test_users.robot <<EOF
*** Settings ***
Library    RequestsLibrary

*** Test Cases ***
Get Users List
    Create Session    myapi    https://reqres.in
    ${response}=    GET    myapi    /api/users?page=2
    Should Be Equal As Integers    ${response.status_code}    200
EOF

# Create README
cat > README.md <<EOF
# Robot Framework Project

## 📦 Setup
1. Create virtual environment:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run tests:
   \`\`\`bash
   robot --outputdir results tests/
   \`\`\`

## 📁 Structure
- tests/ → test cases (web, api)
- resources/ → reusable keywords & variables
- results/ → output logs/reports
EOF

echo "✅ Robot Framework project initialized successfully!"
