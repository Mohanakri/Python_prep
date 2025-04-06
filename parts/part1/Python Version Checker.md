Write a Python program to find out what version of Python you are using.

A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. This string is displayed when the interactive interpreter is started.

Version info:

A tuple containing the five components of the version number: major, minor, micro, releaselevel, and serial. All values except releaselevel are integers; the release level is 'alpha', 'beta', 'candidate', or 'final'. The version_info value corresponding to the Python version 2.0 is (2, 0, 0, 'final', 0). The components can also be accessed by name, so sys.version_info[0] is equivalent to sys.version_info.major and so on.

Note : 'sys' module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.


For more Practice: Solve these Related Problems:

Write a Python program to check if the installed Python version is greater than 3.6.
Write a Python script to check if the Python version supports a specific module (e.g., f-strings).
Write a Python program to print both the Python version and the implementation name (CPython, PyPy, etc.).
Write a script to compare the installed Python version with a required minimum version and print a warning if it's outdated.
--------------------------------


Absolutely! Below is a **Python program** that covers **all the concepts** you asked for, using the `sys` and `platform` modules.

---

### ✅ What This Program Does:

1. Shows full Python version info (build, compiler, etc.)
2. Displays the structured version info (tuple)
3. Checks if Python version is **greater than 3.6**
4. Checks for support of **f-strings**
5. Prints the **Python implementation name** (e.g., CPython, PyPy)
6. Compares with a **required minimum version** and warns if outdated

---

### 🐍 Python Program:

```python
import sys
import platform

def print_full_version():
    """Print the full Python version string."""
    print("📦 Python Full Version Info:")
    print(sys.version)
    print()

def print_structured_version():
    """Print the structured version info tuple."""
    print("🔢 Version Info Tuple:")
    print("Version Info:", sys.version_info)
    print("Major:", sys.version_info.major)
    print("Minor:", sys.version_info.minor)
    print("Micro:", sys.version_info.micro)
    print("Release Level:", sys.version_info.releaselevel)
    print("Serial:", sys.version_info.serial)
    print()

def check_version_greater_than_36():
    """Check if Python version is greater than 3.6."""
    print("✅ Python Version Check (>= 3.6):")
    if sys.version_info >= (3, 6):
        print("Yes, your Python version is 3.6 or newer.")
    else:
        print("No, your Python version is older than 3.6.")
    print()

def check_fstring_support():
    """Check if f-strings are supported."""
    print("🧪 f-String Support Check:")
    try:
        test = eval('f"f-strings are supported in Python {sys.version_info.major}.{sys.version_info.minor}"')
        print(test)
    except SyntaxError:
        print("f-strings are not supported in this Python version.")
    print()

def print_implementation_name():
    """Print the name of the Python implementation (CPython, PyPy, etc.)."""
    print("⚙️ Python Implementation:")
    print(platform.python_implementation())
    print()

def compare_with_min_required_version(min_version=(3, 8)):
    """Compare installed version with a required minimum and warn if outdated."""
    print("🛠️ Version Comparison:")
    current = sys.version_info
    if current >= min_version:
        print(f"Your Python version ({current.major}.{current.minor}) meets the minimum requirement.")
    else:
        print(f"⚠️ WARNING: Your Python version ({current.major}.{current.minor}) is lower than the required {min_version[0]}.{min_version[1]}")
    print()

def main():
    print_full_version()
    print_structured_version()
    check_version_greater_than_36()
    check_fstring_support()
    print_implementation_name()
    compare_with_min_required_version(min_version=(3, 8))

if __name__ == "__main__":
    main()
```

---

### 🖨️ Sample Output (on Python 3.11, CPython):

```
📦 Python Full Version Info:
3.11.7 (main, Dec  5 2023, 09:30:23) [GCC 12.2.0]

🔢 Version Info Tuple:
Version Info: sys.version_info(major=3, minor=11, micro=7, releaselevel='final', serial=0)
Major: 3
Minor: 11
Micro: 7
Release Level: final
Serial: 0

✅ Python Version Check (>= 3.6):
Yes, your Python version is 3.6 or newer.

🧪 f-String Support Check:
f-strings are supported in Python 3.11

⚙️ Python Implementation:
CPython

🛠️ Version Comparison:
Your Python version (3.11) meets the minimum requirement.
```

---

Let me know if you want this:
- As a `.py` file download
- Extended to check for specific module support
- Auto-update or install logic for older versions

🧰🔧 Happy coding!
