Absolutely! Let's build **multiple programs** for the **Area of a Circle** using various **Object-Oriented Programming (OOP) concepts** in Python.

---

## 🔁 1. **Encapsulation**
Encapsulation = Bundling data + methods, and hiding implementation details.

```python
class Circle:
    def __init__(self, radius):
        self.__radius = radius  # private attribute
        self.__pi = 3.14159      # private constant

    def get_area(self):
        return self.__pi * self.__radius ** 2

# Usage
c = Circle(5)
print("Encapsulated Area:", c.get_area())
```

---

## 🏷️ 2. **Inheritance**
Inheritance = One class inherits properties of another.

```python
class Shape:
    def __init__(self):
        self.name = "Shape"

    def describe(self):
        return f"This is a {self.name}"

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
c = Circle(3)
print(c.describe())
print("Inherited Area:", c.area())
```

---

## 🌀 3. **Polymorphism**
Polymorphism = Same method name, different behavior.

```python
class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

class Square:
    def area(self, side):
        return side ** 2

# Usage
shapes = [Circle(), Square()]
for shape in shapes:
    print("Polymorphic Area:", shape.area(5))
```

---

## 🧱 4. **Abstraction**
Abstraction = Hide complexity via abstract base classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
c = Circle(4)
print("Abstract Area:", c.area())
```

---

## 📦 5. **Class with Static Method**
Sometimes useful to use static methods to calculate area without instantiating.

```python
class Circle:
    @staticmethod
    def area(radius):
        return 3.14 * radius ** 2

print("Static Method Area:", Circle.area(6))
```

---

## 🧪 6. **Class with Class Method**
Useful for using class-level info (like constant π).

```python
class Circle:
    pi = 3.14159

    @classmethod
    def area(cls, radius):
        return cls.pi * radius ** 2

print("Class Method Area:", Circle.area(7))
```

---

## 🧼 7. **Multiple Circles Using Object List**

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Multiple instances
radii = [2, 4, 6]
circles = [Circle(r) for r in radii]

for c in circles:
    print(f"Circle of radius {c.radius} has area {c.area()}")
```

---

Would you like a combined project that includes all OOP concepts in one full real-world-style class?
