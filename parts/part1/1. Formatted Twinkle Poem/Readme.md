# Python Program: Formatted String Output

Write a Python program to print the following string in a specific format (see the output).

Sample String: "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

The print statement (Python 2.6) has been replaced with a print() function (Python 2.6), with keyword arguments to replace most of the special syntax of the old print statement.

For more Practice: Solve these Related Problems:

- Write a Python program to print a multi-line poem using indentation similar to the given format.
- Modify the given poem format to include random spacing and indentation for each line.
- Write a Python program that takes a poem as input and formats it dynamically using a predefined pattern.
- Write a Python script that converts a plain-text poem into a formatted, indented version using tab spaces.

The print() function doesn’t support the “softspace” feature of the old print statement. For example, in Python 2.x, print "A\n", "B" would write "A\nB\n"; but in Python 3.0, print("A\n", "B") writes "A\n B\n".
Initially, you’ll be finding yourself typing the old print x a lot in interactive mode. Time to retrain your fingers to type print(x) instead!
When using the 2to3 source-to-source conversion tool, all print statements are automatically converted to print() function calls, so this is mostly a non-issue for larger projects.
