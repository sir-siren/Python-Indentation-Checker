# Python Indentation Checker
This repository contains a Python script that can be used to check for indentation errors in your Python files. The script uses the `pycodestyle` library to perform a style check on the code and outputs any indentation errors found.

### Requirements
Before using the script, make sure that you have installed the following requirements:

1. Python 3.x
2. `pycodestyle` library (can be installed using `pip install pycodestyle`)

## Usage
The script can be used as follows:

1. Download or clone this repository to your local machine.
2. Open the `python-indentation-checker.py` file in a text editor.
3. Change the `filename` variable to the actual name of your Python file. For example, if your file is named `main.py`, change the line to `filename = "main.py"`.
4. Save the changes to the file.
5. Open a terminal or command prompt and navigate to the directory containing the script.
6. Run the script by typing `python python-indentation-checker.py` in the terminal or command prompt and press Enter.
7. The script will perform a style check on the code and output any indentation errors found. If no indentation errors are found, a message indicating that no errors were detected will be displayed.

## Example Output
Here is an example of what the output of the script might look like:
```py
Indentation errors found:
Line 2: E111 indentation is not a multiple of four
Line 4: E111 indentation is not a multiple of four
Line 8: E111 indentation is not a multiple of four
Line 10: E112 expected an indented block
Line 15: E111 indentation is not a multiple of four
Line 16: E111 indentation is not a multiple of four
Line 19: E112 expected an indented block
```

## Troubleshooting
If you encounter any issues while using the script, please check the following:

1. Make sure that you have installed the required dependencies.
2. Make sure that you have specified the correct name of your Python file in the `filename` variable.
3. Make sure that the file exists in the same directory as the script.

## Conclusion
The Python Indentation Checker script provides an easy way to check for indentation errors in your Python code. By using `pycodestyle`, the script is able to perform a style check on the code and output any errors found, making it a useful tool for maintaining the quality of your code.
