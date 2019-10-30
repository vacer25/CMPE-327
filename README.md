# CMPE 327
Code for CISC/CMPE 327 Software Quality Assurance Course

[![](https://github.com/vacer25/CMPE-327/workflows/Master%20Test/badge.svg)](https://github.com/vacer25/CMPE-327/actions)

## Custom system testing script
This project shows how to preform system testing of a python script without using pytest

The [system_test_runner.py](system-test/system_test_runner.py) script is designed for the ELEC 327 frontend system testing assignment and handles lots of special cases that might be useful for the different test cases required.

## Getting started:

### Installation:

1. Download/clone this repository
2. In root folder, run:<br>

        pip install -r requirements.txt

### Basic usage:</br>
- Windows:</br>

        system-test-frontend.bat

- Cross-platform:</br>

        cd system-test
        python system_test_runner.py ../src/frontend.py

If everything goes well, you shoud get this output for the example test cases included in this repository:

<img src="docs/example_testcases_all_passed.png" alt="Example Testcases All Passed"/>

## Testing approach:

### Folder structure:

The source code is in the `src` folder

The system tests are in the `system-test` folder</br>
The structure of this folder must be as shown below:

<img src="docs/folder_structure.png" alt="Folder Structure"/>

### Testing precedure:

The [system_test_runner.py](system-test/system_test_runner.py) script recursively traverses the `system-test` folder.
       
For each `system-test/Rx/Ty` folder, this script will:

1. Run the frontend script being tested, passing the appropriate valid accounts file (as described below) and transaction summary file as `RxTy.out.actual.txt`
2. Pipe the inputs from the `RxTy.input.txt` file (line-by-line) into the front-end application
3. Save all console output to the `RxTy.console.actual.txt` file
4. Compare the `RxTy.console.actual.txt` file to the `RxTy.console.expected.txt` file
5. If any lines differ, indicate that this test failed and output all lines that differ to the console
6. Compare the `RxTy.out.actual.txt` file to the `RxTy.out.expected.txt` file if it exists or verify that no output file was created if `none.console.expected.txt` exists in the current test case folder
7. If any lines differ, indicate that this test failed and output all lines that differ to the console

For each test case, the default valid accounts list file is the common one in the `system-test` folder.
This behaviour is overridden if:
- The test case folder contails a local `valid_accounts.txt` file, in this case the local file is used.
- The test case folder contails a local `.no_valid_accounts` file, in this case a non-existant file is used to simulate the valid account list file not existing.

## Adding test cases:

For each requirement, create a `Rx` folder in the `system-test` folder when x is the requirement number.</br>
For each test case of the requirement, create a `Ty` folder in the `Rx` folder when y is the test case number.

Each test case folder must contain three files:
- `RxTy.input.txt` containing the console input lines (each on each own line)
- `RxTy.console.expected.txt` containing the expected console output
- `RxTy.out.expected.txt` or `none.console.expected.txt` containing the expected contents of the transaction summary file

For generating the expected files, it is recommended to look at the default example test cases in this repository.

These folders will be automatically found, just make sure to save the above files before re-running the test script.

### Command line options:
Usage: `system_test_runner.py [-h] [-c #] [-d] scriptToTestFileName`

#### Required:

  `scriptToTestFileName`</br>
  The path & name of the script to be tested, can be relative

#### Optional:

  `-h`</br>
  Show this help message and exit

  `-c #`</br>
  Set the amount of surrounding lines to include for context in diff output (default is 1)

  `-d`</br>
  Set to automatically delete generated output files after test case is done, if this is not set all the generated output files are kept

### Misc.
- Feel free to create an issue if something does not make sense
- Pull requests welcome
