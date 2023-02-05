import pycodestyle

# The filename should be changed to the actual name of your Python file
filename = "main.py"

try:
    with open(filename) as f:
        code = f.read()
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    # Exit the program
    exit(1)

# Check the code for any style issues using pycodestyle
checker = pycodestyle.Checker(filename, show_source=True)
report = checker.check_all(code)

if report == 0:
    print("No indentation errors found.")
else:
    print("Indentation errors found.")
