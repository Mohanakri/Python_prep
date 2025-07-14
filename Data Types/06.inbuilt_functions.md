Here’s a table of **important built-in Python functions** that are most useful in **intermediate to advanced** development tasks — with **description** and **example**:

---

### ✅ **Advanced Built-in Python Functions**

| **Function**                             | **Description**                                           | **Example**                                      |
| ---------------------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| `map(func, iterable)`                    | Applies a function to each item in an iterable            | `map(str.upper, ['a', 'b']) → ['A', 'B']`        |
| `filter(func, iterable)`                 | Filters elements that return `True` from the function     | `filter(lambda x: x > 0, [-1, 2]) → [2]`         |
| `zip(*iterables)`                        | Combines iterables element-wise into tuples               | `zip([1, 2], ['a', 'b']) → [(1, 'a'), (2, 'b')]` |
| `enumerate(iterable)`                    | Adds index to iterable, returns `(index, value)` tuples   | `enumerate(['a', 'b']) → [(0, 'a'), (1, 'b')]`   |
| `sorted(iterable, key=..., reverse=...)` | Returns a sorted list                                     | `sorted(['abc', 'a'], key=len) → ['a', 'abc']`   |
| `any(iterable)`                          | `True` if **any** element is true                         | `any([0, False, 5]) → True`                      |
| `all(iterable)`                          | `True` if **all** elements are true                       | `all([1, True, 3]) → True`                       |
| `reversed(seq)`                          | Returns a reversed iterator                               | `list(reversed([1, 2, 3])) → [3, 2, 1]`          |
| `len(obj)`                               | Returns number of items                                   | `len("hello") → 5`                               |
| `sum(iterable)`                          | Returns sum of all elements                               | `sum([1, 2, 3]) → 6`                             |
| `min(iterable)`                          | Minimum value                                             | `min([3, 1, 2]) → 1`                             |
| `max(iterable)`                          | Maximum value                                             | `max([3, 1, 2]) → 3`                             |
| `abs(x)`                                 | Absolute value                                            | `abs(-4) → 4`                                    |
| `round(x, ndigits)`                      | Rounds a number to given digits                           | `round(3.14159, 2) → 3.14`                       |
| `divmod(a, b)`                           | Returns tuple `(a // b, a % b)`                           | `divmod(8, 3) → (2, 2)`                          |
| `isinstance(obj, type)`                  | Checks if object is of specified type                     | `isinstance(5, int) → True`                      |
| `type(obj)`                              | Returns the type of an object                             | `type([1, 2]) → <class 'list'>`                  |
| `eval(expr)`                             | Evaluates a string as Python expression *(use carefully)* | `eval("3 + 5") → 8`                              |
| `input()`                                | Reads a line from input as string                         | `input("Enter name: ")`                          |
| `print()`                                | Prints to console                                         | `print("Hello")`                                 |
| `range(start, stop)`                     | Generates a sequence of numbers                           | `range(1, 5) → [1, 2, 3, 4]` (with `list()`)     |

---

Let me know if you want:

* A printable PDF version
* A Python cheat sheet notebook
* A quiz or flashcards to test yourself
