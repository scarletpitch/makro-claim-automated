# Utilities

`UtilitiesLibrary` for solve general problem in automation test.

```
Version: 1.0.0

Last Update: 30-Nov-2020
```

---

### Installation

Install required libraries with command as below before use `UtilitiesLibrary`.

```sh
pip install -r requirements.txt
```

[requirements.txt](/requirements.txt)

```
dictdiffer==0.8.1
pylint==2.5.3
pytz==2020.1
requests==2.24.0
robotframework>=3.1.2
```

--- 

### Usage

To use `UtilitiesLibrary` in Robot Framework tests, the library needs to first be imported using the Library setting as any other library. 

```
*** Setting ***
Documentation   Simple example using Utilities
Library         UtilitiesLibrary

*** Test Cases ***
Call Utilities
    ${gen_id} =  Generate Request UID  XXX_APP
```

The above example that you can execute on your machine. [Here](docs/Utilities.html) for more keywords inside `UtilitiesLibrary`.
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
robot -P .\..\ .\DictManagementTest.robot
robot -P .\..\ .\DtManagementTest.robot
robot -P .\..\ .\SocketManagementTest.robot
robot -P .\..\ .\TagGeneratorTest.robot
robot -P .\..\ .\UtilitiesTest.robot
```

`TESTS`: Command to run script unit test in python scripts.

```sh
# go to tests
cd tests

# run all
sh __run_test.sh

# or run each method
python DictManagementTest.py
python DtManagementTest.py
python SocketManagementTest.py
python TagGeneratorTest.py
python UtilitiesTest.py
```

---

### Use Library as Submodule
Submodule repository `UtilitiesLibrary`. Click [Here](https://kscm.kasikornbank.com:8443/automation/automation-shared-library/utilities-library)
We’ll walk through developing a simple project that has been split up into a main project and a few sub-projects.

Let’s start by adding an existing Git repository as a submodule of the repository that we’re working on. To add a new submodule you use the git submodule add command with the absolute or relative URL of the project you would like to start tracking. In this example, we’ll add a library called `UtilitiesLibrary`.
```
mkdir libs
cd libs
git submodule add https://kscm.kasikornbank.com:8443/automation/automation-shared-library/utilities-library.git
```

About this solution and In the future, you can continue to make better contributions to this common library.

---