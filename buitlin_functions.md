Great question! Python provides a rich set of **built-in functions** that you can use without importing any libraries. Here's a handy list of the **most commonly used built-in functions** in Python:

---

### ✅ **Most Common Built-in Functions (with examples)**

| Function | Description | Example |
|----------|-------------|---------|
| `print()` | Displays output | `print("Hello")` |
| `len()` | Returns length of iterable | `len([1, 2, 3]) → 3` |
| `type()` | Returns the type of a variable | `type(5) → <class 'int'>` |
| `int()` | Converts to integer | `int("5") → 5` |
| `float()` | Converts to float | `float("3.14") → 3.14` |
| `str()` | Converts to string | `str(100) → "100"` |
| `list()` | Creates a list | `list("abc") → ['a', 'b', 'c']` |
| `dict()` | Creates a dictionary | `dict(name="John") → {'name': 'John'}` |
| `set()` | Creates a set | `set([1, 2, 2]) → {1, 2}` |
| `tuple()` | Creates a tuple | `tuple([1, 2]) → (1, 2)` |
| `range()` | Creates a sequence of numbers | `range(5) → 0 to 4` |
| `sum()` | Returns the sum of elements | `sum([1, 2, 3]) → 6` |
| `max()` | Returns the largest item | `max([4, 7, 1]) → 7` |
| `min()` | Returns the smallest item | `min([4, 7, 1]) → 1` |
| `abs()` | Absolute value | `abs(-10) → 10` |
| `round()` | Rounds a number | `round(3.14159, 2) → 3.14` |
| `sorted()` | Returns a sorted list | `sorted([3, 1, 2]) → [1, 2, 3]` |
| `reversed()` | Returns reversed iterator | `list(reversed([1, 2, 3])) → [3, 2, 1]` |
| `enumerate()` | Returns index-value pairs | `for i, v in enumerate(['a', 'b']):` |
| `zip()` | Combine iterables into tuples | `list(zip([1,2], ['a','b'])) → [(1,'a'),(2,'b')]` |
| `map()` | Applies a function to each item | `map(str, [1, 2]) → ['1', '2']` |
| `filter()` | Filters items using a function | `filter(lambda x: x%2==0, [1,2,3]) → [2]` |
| `input()` | Takes input from user | `input("Enter name: ")` |
| `help()` | Shows documentation | `help(len)` |
| `isinstance()` | Checks object type | `isinstance(10, int) → True` |
| `id()` | Returns memory address | `id(x)` |

---

### 🔁 You can view all built-in functions in Python using:

```python
print(dir(__builtins__))
```

Would you like a PDF or cheat sheet version of these built-ins too? Or a quiz to test your knowledge? 😄
