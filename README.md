# Robot Framework Project

## 📦 Setup
1. Create virtual environment:
   ```bash
   //Go to project folder
   cd ~/makro-claim-automated
   
   python3.12 -m venv venv
   source venv/bin/activate
   pip install webdriver-manager
   pip install -U selenium robotframework-seleniumlibrary webdriver-manager
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   robot example.robot
   ../makro-claim-automated/venv/bin/python3 -m robot --pythonpath resources keywords/web/test_login.robot
   ```



## 📁 Structure
- tests/ → test cases (web, api)
- resources/ → reusable keywords & variables
- results/ → output logs/reports

## 🔹 Branch Roles
| Branch      | Purpose                                                                 | Example Name                |
|------------|-------------------------------------------------------------------------|----------------------------|
| main       | Stores production-ready code that has been deployed.                   | main                       |
| develop    | Collects all features ready for testing before release.                | develop                    |
| feature/   | Used for developing individual new features.                            | feature/login, feature/add-project |
| release/   | Used to prepare a release, run final tests, and fix small bugs before merging into main. | release/v1.0.0 |
| hotfix/    | Used to quickly fix critical bugs found in production.                 | hotfix/fix-login-bug       |

## 🧩 Setup ChromeDriver
1. Download ChromeDriver for your OS version:
   https://googlechromelabs.github.io/chrome-for-testing/
2. Extract it to: `./chromedriver-mac-arm64`

# makro-claim-automated
