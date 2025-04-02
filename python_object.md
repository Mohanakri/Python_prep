Are All Things in Python Objects?

Yes! Everything in Python is an object.

Functions → Objects

Classes → Objects

Data types (int, str, list, etc.) → Objects

Modules → Objects

Even None, True, and False → Objects


Since Python is object-oriented, every entity in Python is an instance of a class, making everything an object.


---

1. Checking If Everything Is an Object

You can verify that everything in Python is an object using isinstance():

print(isinstance(10, object))  # True (int is an object)
print(isinstance("Hello", object))  # True (str is an object)
print(isinstance([1, 2, 3], object))  # True (list is an object)
print(isinstance(lambda x: x * 2, object))  # True (function is an object)
print(isinstance(None, object))  # True (None is an object)

Since all return True, we confirm that everything in Python is an object.


---

2. What is an Object in Python?

An object in Python is an instance of a class.
Every object has:

Identity → A unique ID (id(obj))

Type → Its class (type(obj))

Attributes & Methods → Defined by its class


Example: Checking Object Identity

x = 10
print(id(x))  # Unique memory ID
print(type(x))  # <class 'int'>


---

3. Object-Oriented Nature of Python

Since everything is an object, Python follows object-oriented programming (OOP) principles.

A. Numbers and Strings Are Objects

print((10).__class__)  # <class 'int'>
print(("hello").__class__)  # <class 'str'>

B. Functions Are Objects

def greet():
    print("Hello")

print(type(greet))  # <class 'function'>

Since functions are objects, they can be stored in variables or passed as arguments.

C. Classes Are Also Objects

class Person:
    pass

print(type(Person))  # <class 'type'> (even classes are objects!)

D. Modules Are Objects

import math
print(type(math))  # <class 'module'>


---

4. Everything in Python Derives from object

All classes in Python inherit from object (the base class for all objects).

print(issubclass(int, object))  # True
print(issubclass(str, object))  # True
print(issubclass(list, object))  # True
print(issubclass(dict, object))  # True

Even user-defined classes inherit from object:

class MyClass:
    pass

print(issubclass(MyClass, object))  # True


---

5. Conclusion

✔ Everything in Python is an object (functions, classes, numbers, strings, lists, etc.).
✔ Python follows object-oriented programming (OOP).
✔ All objects inherit from object class.

Would you like an example of how Python internally represents objects in memory?

