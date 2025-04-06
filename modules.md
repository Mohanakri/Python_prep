Here’s a list of commonly used Python modules, grouped by purpose, that are widely used in interviews, real-world projects, and production code:


---

1. Built-in Standard Library Modules (No installation needed)

General Utility

math – for mathematical functions

random – for generating random numbers

datetime – for date and time manipulation

time – for time-related functions (e.g., sleep, timestamps)

os – for interacting with the operating system

sys – for system-specific parameters and functions

functools – for higher-order functions like reduce, lru_cache

itertools – for efficient looping and combinatorics

collections – for advanced data structures (e.g., Counter, deque, defaultdict)

re – for regular expressions


File Handling / Data Processing

json – to work with JSON data

csv – to read/write CSV files

pickle – for object serialization


Debugging and Profiling

logging – for logging messages

traceback – for printing error stack traces

cProfile – for profiling code performance



---

2. External (Third-party) Modules (Require installation)

Data Analysis / Machine Learning

numpy – for numerical operations

pandas – for data analysis and manipulation

matplotlib, seaborn – for data visualization

scikit-learn – for machine learning

tensorflow, pytorch – for deep learning


Web and APIs

requests – for HTTP requests

flask / fastapi – for building REST APIs

beautifulsoup4, scrapy – for web scraping


Automation / DevOps

boto3 – AWS automation

paramiko – SSH automation

subprocess – run shell commands

fabric – remote server automation


Testing

unittest – built-in testing framework

pytest – popular third-party testing tool

mock – for mocking objects in tests



---

Would you like a small project idea using most of these common modules to practice?

_---------------------
Great question! Here's the deal:

Yes, even if a module is built-in, you still need to import it to use its functions, classes, or constants — unless it's part of Python's core built-ins that are loaded by default.


---

Modules that require import (even though they’re built-in):

These are part of the Python Standard Library, but not loaded automatically:

import math
import datetime
import random
import os
import sys
import re
import collections
import functools
import itertools

You must import them before use:

import math
print(math.sqrt(25))  # works

# print(sqrt(25))  # ❌ NameError: name 'sqrt' is not defined


---

Functions you can use without importing anything:

These come from Python’s core built-ins (auto-loaded):

print()

len()

sum()

range()

max(), min()

int(), float(), str()

list(), dict(), set(), tuple()

abs(), round()

input()

type(), isinstance(), id(), dir()


No import is needed for these:

print(len([1, 2, 3]))


---

TL;DR

Built-in module? Yes, still need import.

Core built-in functions? No import needed.


Want a cheat sheet that separates both with examples?

