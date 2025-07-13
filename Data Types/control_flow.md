Awesome! Here's the extended version of the table, now including:

1. ✅ Basic Data Types


2. ✅ Collection Types


3. ✅ Loop Examples (for, while)


4. ✅ Output within table


5. ✅ List Comprehension


6. ✅ Dictionary Comprehension


7. ✅ Nested Collection Looping




---

📘 Python Data Types, Collection Types, Loops, Comprehensions (with Syntax & Output)


---

🔢 Basic Data Types

Data Type	Description	Syntax & Example	for Loop Example + Output	while Loop Example + Output

int	Integer	x = 3	for i in range(x): print(i)<br>▶️ Output:<br>0<br>1<br>2	i = 0; while i < x:<br> print(i); i += 1<br>▶️ Output:<br>0<br>1<br>2
float	Decimal	pi = 3.14	for i in range(2): print(pi)<br>▶️ Output:<br>3.14<br>3.14	i = 0; while i < 2:<br> print(pi); i += 1<br>▶️ Output:<br>3.14<br>3.14
str	Text	name = "Max"	for ch in name: print(ch)<br>▶️ Output:<br>M<br>a<br>x	i = 0; while i < len(name):<br> print(name[i]); i += 1<br>▶️ Output:<br>M<br>a<br>x
bool	Boolean	flag = True	if flag: print("Yes")<br>▶️ Output:<br>Yes	while flag:<br> print("Yes"); flag = False<br>▶️ Output:<br>Yes
complex	Complex	z = 2 + 3j	print(z.real, z.imag)<br>▶️ Output:<br>2.0 3.0	print(z.real)<br>print(z.imag)<br>▶️ Output:<br>2.0<br>3.0
None	Null	x = None	if x is None: print("None")<br>▶️ Output:<br>None	while x is None:<br> print("None"); break<br>▶️ Output:<br>None



---

📦 Collection Data Types

Data Type	Description	Syntax & Example	for Loop Example + Output	while Loop Example + Output

list	Ordered, mutable	nums = [10, 20, 30]	for n in nums: print(n)<br>▶️ Output:<br>10<br>20<br>30	i = 0; while i < len(nums):<br> print(nums[i]); i += 1<br>▶️ Output:<br>10<br>20<br>30
tuple	Ordered, immutable	vals = (1, 2, 3)	for v in vals: print(v)<br>▶️ Output:<br>1<br>2<br>3	i = 0; while i < len(vals):<br> print(vals[i]); i += 1<br>▶️ Output:<br>1<br>2<br>3
set	Unordered, unique	colors = {'red', 'blue'}	for c in colors: print(c)<br>▶️ Output:<br>red<br>blue (order may vary)	colors = list(colors)<br>i = 0; while i < len(colors):<br> print(colors[i]); i += 1<br>▶️ Output:<br>red<br>blue
dict	Key-value pairs	person = {'name': 'Sam', 'age': 25}	for k in person:<br> print(k, person[k])<br>▶️ Output:<br>name Sam<br>age 25	keys = list(person)<br>i = 0; while i < len(keys):<br> print(keys[i], person[keys[i]]); i += 1<br>▶️ Output:<br>name Sam<br>age 25



---

🧠 List Comprehension

Concept	Syntax & Example	Output

Simple List Comp	[x*2 for x in range(3)]	[0, 2, 4]
With Condition	[x for x in range(5) if x % 2 == 0]	[0, 2, 4]
Nested Loop	[i*j for i in range(1, 3) for j in range(1, 3)]	[1, 2, 2, 4]



---

🧠 Dictionary Comprehension

Concept	Syntax & Example	Output

Key-Value Square	{x: x**2 for x in range(3)}	{0: 0, 1: 1, 2: 4}
Invert Dict	{v: k for k, v in {'a':1, 'b':2}.items()}	{1: 'a', 2: 'b'}



---

🧱 Nested Collection Looping

Collection	Syntax	Output

Nested List	matrix = [[1,2], [3,4]]<br>for row in matrix:<br>  for val in row: print(val)	1<br>2<br>3<br>4
Dict of Lists	data = {'a': [1,2], 'b':[3,4]}<br>for k in data:<br>  for val in data[k]: print(k, val)	a 1<br>a 2<br>b 3<br>b 4



---

Would you like this as a downloadable README.md file now?

