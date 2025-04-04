Here's a **comprehensive Python program** that demonstrates the use of **all list class methods** and **special methods (`__getitem__`, `__setitem__`, etc.)**.  

### **Python Program Using All List Methods & Special Methods**
```python
class MyList:
    def __init__(self, data=None):
        self.data = data if data else []  # Initialize with an empty list if no data provided

    def __repr__(self):
        return f"MyList({self.data})"  # String representation

    def __len__(self):
        return len(self.data)  # Returns the length of the list

    def __getitem__(self, index):
        return self.data[index]  # Gets an item or slice

    def __setitem__(self, index, value):
        self.data[index] = value  # Sets an item

    def __delitem__(self, index):
        del self.data[index]  # Deletes an item

    def __iter__(self):
        return iter(self.data)  # Makes the list iterable

    def __contains__(self, item):
        return item in self.data  # Checks if an item exists

    def __add__(self, other):
        if isinstance(other, MyList):
            return MyList(self.data + other.data)  # List concatenation
        return NotImplemented

    def __mul__(self, times):
        return MyList(self.data * times)  # List repetition

    # Implementing all list methods
    def append(self, item):
        self.data.append(item)

    def extend(self, iterable):
        self.data.extend(iterable)

    def insert(self, index, item):
        self.data.insert(index, item)

    def remove(self, item):
        self.data.remove(item)

    def pop(self, index=-1):
        return self.data.pop(index)

    def clear(self):
        self.data.clear()

    def index(self, item):
        return self.data.index(item)

    def count(self, item):
        return self.data.count(item)

    def sort(self, reverse=False):
        self.data.sort(reverse=reverse)

    def reverse(self):
        self.data.reverse()

    def copy(self):
        return MyList(self.data.copy())  # Returns a copy of the list

# Using the MyList class
my_list = MyList([10, 20, 30, 40, 50])

# Special Methods
print("Original List:", my_list)
print("Length:", len(my_list))
print("Item at index 2:", my_list[2])
my_list[1] = 25
print("After setting index 1:", my_list)
del my_list[3]
print("After deleting index 3:", my_list)

# Iteration
print("Iterating over list:")
for item in my_list:
    print(item, end=" ")

print("\nIs 25 in the list?", 25 in my_list)

# List Methods
my_list.append(60)
print("\nAfter append:", my_list)

my_list.extend([70, 80])
print("After extend:", my_list)

my_list.insert(2, 22)
print("After insert:", my_list)

my_list.remove(22)
print("After remove:", my_list)

print("Popped item:", my_list.pop())
print("After pop:", my_list)

print("Index of 30:", my_list.index(30))
print("Count of 25:", my_list.count(25))

my_list.sort()
print("After sorting:", my_list)

my_list.reverse()
print("After reversing:", my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)

# List Operations
new_list = my_list + MyList([90, 100])
print("After concatenation:", new_list)

repeated_list = my_list * 2
print("After repetition:", repeated_list)

my_list.clear()
print("After clear:", my_list)
```

---

### **Explanation**
- This program defines a **custom list class (`MyList`)** that mimics Python's built-in `list` behavior.
- It implements **special methods (`__getitem__`, `__setitem__`, `__iter__`, `__contains__`, `__add__`, etc.)**.
- It provides **all list methods** like `append()`, `extend()`, `insert()`, `remove()`, `sort()`, etc.
- It showcases **list operations like concatenation (`+`) and repetition (`*`)**.
- The output demonstrates **adding, removing, sorting, iterating, and clearing elements**.

---

### **Sample Output**
```
Original List: MyList([10, 20, 30, 40, 50])
Length: 5
Item at index 2: 30
After setting index 1: MyList([10, 25, 30, 40, 50])
After deleting index 3: MyList([10, 25, 30, 50])
Iterating over list:
10 25 30 50 
Is 25 in the list? True

After append: MyList([10, 25, 30, 50, 60])
After extend: MyList([10, 25, 30, 50, 60, 70, 80])
After insert: MyList([10, 25, 22, 30, 50, 60, 70, 80])
After remove: MyList([10, 25, 30, 50, 60, 70, 80])
Popped item: 80
After pop: MyList([10, 25, 30, 50, 60, 70])
Index of 30: 2
Count of 25: 1
After sorting: MyList([10, 25, 30, 50, 60, 70])
After reversing: MyList([70, 60, 50, 30, 25, 10])
Copied list: MyList([70, 60, 50, 30, 25, 10])
After concatenation: MyList([70, 60, 50, 30, 25, 10, 90, 100])
After repetition: MyList([70, 60, 50, 30, 25, 10, 70, 60, 50, 30, 25, 10])
After clear: MyList([])
```

Would you like any modifications or explanations in more depth?
