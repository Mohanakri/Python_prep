Great question! Here's a clear comparison of **`string`, `list`, `set`, `tuple`, and `dictionary`** in Python with key differences in a table format and examples to help you understand when to use each.

---

## 🔍 **Summary Table**

| Feature            | `str` (String)         | `list`                 | `tuple`                | `set`                  | `dict` (Dictionary)           |
|--------------------|------------------------|-------------------------|-------------------------|-------------------------|--------------------------------|
| **Mutable?**       | ❌ No                  | ✅ Yes                  | ❌ No                   | ✅ Yes                  | ✅ Yes                          |
| **Ordered?**       | ✅ Yes (from Python 3.7) | ✅ Yes                 | ✅ Yes                 | ❌ No                   | ✅ Yes                          |
| **Duplicates?**    | ✅ Yes                 | ✅ Yes                 | ✅ Yes                 | ❌ No                   | ❌ Keys must be unique          |
| **Indexed?**       | ✅ Yes                 | ✅ Yes                 | ✅ Yes                 | ❌ No                   | ✅ Keys are used as index       |
| **Use-case**       | Text                   | List of items           | Fixed list of items     | Unique values            | Key-value mapping              |
| **Syntax**         | `"hello"`              | `[1, 2, 3]`             | `(1, 2, 3)`             | `{1, 2, 3}`              | `{"a": 1, "b": 2}`             |

---

## 🔸 **1. String (`str`)**
- A sequence of characters.
- Immutable (cannot be changed).
```python
s = "hello"
print(s[1])     # e
```

---

## 🔸 **2. List (`list`)**
- Ordered and **mutable** (can be changed).
- Allows duplicates and any data type.
```python
l = [1, 2, 3, 2]
l.append(4)
print(l[2])     # 3
```

---

## 🔸 **3. Tuple (`tuple`)**
- Ordered and **immutable** (cannot be changed after creation).
- Useful for fixed collections (e.g., coordinates).
```python
t = (1, 2, 3)
print(t[1])     # 2
```

---

## 🔸 **4. Set (`set`)**
- **Unordered**, no duplicates.
- Useful when you want unique values.
```python
s = {1, 2, 2, 3}
print(s)        # {1, 2, 3}
s.add(4)
```

---

## 🔸 **5. Dictionary (`dict`)**
- Stores **key-value** pairs.
- Keys must be unique and immutable; values can be anything.
```python
d = {"name": "Ravi", "age": 30}
print(d["name"])  # Ravi
d["age"] = 31     # Update
```

---

## ✅ **When to Use What?**

| Task                                 | Data Structure |
|--------------------------------------|----------------|
| Store characters or text             | `str`          |
| List of items with order             | `list`         |
| Fixed set of values (e.g., RGB)      | `tuple`        |
| Unique values only                   | `set`          |
| Key-value lookup (e.g., user info)   | `dict`         |

---

Want code examples for all with **mutability demo** or **interconversion** (like list to set, dict to list)?
