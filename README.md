# CMPE-327
Code for ELEC 327 Software Quality Assurance Course

[![](https://github.com/vacer25/CMPE-327/workflows/Master%20Test/badge.svg)](https://github.com/vacer25/CMPE-327/actions)

## Custom system testing script
This project shows how to preform system testing of a python script without using pytest

The [system-test-runner.py](system-test/system-test-runner.py) script is designed for the ELEC 327 frontend system testing assignment and handles lots of special cases that might be useful for the different test cases required.

### To install:

1. Download/clone this repository
2. In root folder, run:<br>

        pip install -r requirements.txt

### To use:</br>
- Windows:</br>

        system-test-frontend.bat

- Cross-platform:</br>

        cd system-tests
        python system_test_runner.py ../src/frontend.py

If everything goes well, you shoud get this:

<img src="docs/example_testcases_all_passed.png" alt="Example Testcases All Passed.png"/>

