# ExcelImportLibrary

`ExcelImportLibrary` for support XLSX test data to use in test case or generate test scripts.

---

### Installation

Install required libraries with command as below before use `ExcelImportLirary`

```sh
pip install -r requirements.txt
```

[requirements.txt](/requirements.txt)

```
openpyxl~=3.0.3
robotframework~=3.1.2
robotframework-excellib>=2.0.1
```

--- 

### Usage

To use `ExcelImportLibrary` in Robot Framework tests, the library needs to first be imported using the Library setting as any other library. 

```
*** Setting ***
Documentation   Simple example using ExcelImportLibrary
Library         ExcelImportLibrary

*** Test Cases ***
Read Data From Excel
    Open Excel File  test_data.xlsx
    Select Excel Sheet  main
    ${test_data} =  Find Test Case  main  Read Data From Excel  
```

The above example that you can execute on your machine. Click [Here](docs/ExcelImportLibrary.html) for more keywords inside `ExcelImportLibrary`

And command to run script please add option -P to define library location before run test.

```
robot -P path/to/this/library test_script.robot
```
---

### Unit Test 

`ACCEPTANCE`: Command to run script unit test in robot framework scripts.

```sh
# go to acceptance
cd acceptance

# run all
robot -P .\..\ .\
# or
sh _run_test.sh

# or run each method
robot -P .\..\ .\ExcelImportTest.robot
robot -P .\..\ .\ExcelUpdateTest.robot
```

`TESTS`: Command to run script unit test in python scripts.

```sh
# go to tests
cd tests

# run all
sh __run_test.sh

# or run each method
python ExcelImportTest.py
python ExcelUpdateTest.py
```

---

### Use Library as Submodule
Submodule repository `ExcelImportLibrary`. Click [Here](https://kscm.kasikornbank.com:8443/automation/automation-shared-library/excel-import-library)
We’ll walk through developing a simple project that has been split up into a main project and a few sub-projects.

Let’s start by adding an existing Git repository as a submodule of the repository that we’re working on. To add a new submodule you use the git submodule add command with the absolute or relative URL of the project you would like to start tracking. In this example, we’ll add a library called `ExcelImportLibrary`.
```
mkdir libs
cd libs
git submodule add https://kscm.kasikornbank.com:8443/automation/automation-shared-library/excel-import-library.git
```

About this solution and In the future, you can continue to make better contributions to this common library.

---