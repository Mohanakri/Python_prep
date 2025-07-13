Absolutely! Here's a complete set of solutions for all 60 Python logic-based coding interview questions—well-structured by category: Numbers, Strings, Lists, Dictionaries, Patterns, Intermediate Logic, and Bonus Challenges.


---

🔢 Number-Based Problems (1–10)

# 1. Prime check
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

# 2. Fibonacci series
def fibonacci(n):
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 3. Factorial
def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n-1)

def factorial_iterative(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

# 4. Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

# 5. Palindrome number
def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 6. GCD and LCM
import math
def find_gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a*b)//gcd
    return gcd, lcm

# 7. Decimal to binary/octal/hex
def convert_bases(n):
    return bin(n)[2:], oct(n)[2:], hex(n)[2:]

# 8. Sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 9. Prime numbers in a range
def primes_in_range(start, end):
    return [x for x in range(start, end+1) if is_prime(x)]

# 10. Multiplication table
def multiplication_table(n):
    return [f"{n} x {i} = {n*i}" for i in range(1, 11)]


---

📜 String-Based Problems (11–20)

# 11. String palindrome
def is_string_palindrome(s):
    return s == s[::-1]

# 12. Vowel and consonant count
def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    v = sum(1 for c in s if c in vowels)
    c = sum(1 for c in s if c.isalpha() and c not in vowels)
    return v, c

# 13. Reverse string without slicing
def reverse_string(s):
    result = ''
    for char in s:
        result = char + result
    return result

# 14. Remove duplicates
def remove_duplicates(s):
    seen = set()
    return ''.join([c for c in s if not (c in seen or seen.add(c))])

# 15. Most frequent character
from collections import Counter
def most_frequent_char(s):
    freq = Counter(s)
    return max(freq, key=freq.get)

# 16. Anagram check
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 17. Capitalize first letter
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

# 18. Contains only digits
def is_only_digits(s):
    return s.isdigit()

# 19. Count words manually
def count_words(s):
    count = 0
    in_word = False
    for char in s:
        if char != ' ' and not in_word:
            count += 1
            in_word = True
        elif char == ' ':
            in_word = False
    return count

# 20. All substrings
def all_substrings(s):
    return [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]


---

📋 List/Array Problems (21–30)

# 21. Second largest number
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# 22. Remove duplicates (preserve order)
def remove_duplicates_list(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

# 23. Rotate list
def rotate_list(lst, n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

# 24. Reverse list
def reverse_list(lst):
    return lst[::-1]

# 25. Missing number
def find_missing(lst, total):
    expected_sum = total * (total + 1) // 2
    return expected_sum - sum(lst)

# 26. Count even/odd
def count_even_odd(lst):
    even = sum(1 for x in lst if x % 2 == 0)
    odd = len(lst) - even
    return even, odd

# 27. Separate pos/neg
def separate_pos_neg(lst):
    pos = [x for x in lst if x >= 0]
    neg = [x for x in lst if x < 0]
    return pos, neg

# 28. Common elements
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 29. Flatten nested list
def flatten_list(nested):
    return [item for sublist in nested for item in sublist]

# 30. Group by frequency
from collections import defaultdict
def group_by_frequency(lst):
    freq = defaultdict(list)
    for x in lst:
        freq[lst.count(x)].append(x)
    return dict(freq)


---

🔣 Dictionary/Tuple Logic (31–36)

# 31. Character frequency
def char_frequency(s):
    return dict(Counter(s))

# 32. Merge dictionaries
def merge_dicts(d1, d2):
    return {**d1, **d2}

# 33. Sort dict by values
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

# 34. Invert dict
def invert_dict(d):
    return {v: k for k, v in d.items()}

# 35. Group anagrams
def group_anagrams(words):
    from collections import defaultdict
    anagram_map = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())

# 36. Duplicate values
def find_duplicate_values(d):
    values = list(d.values())
    return [item for item in set(values) if values.count(item) > 1]


---

🔄 Pattern Printing (37–40)

# 37. Pyramid
def print_pyramid(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '*'*(2*i-1))

# 38. Floyd’s triangle
def floyd_triangle(rows):
    num = 1
    for i in range(1, rows+1):
        print(' '.join(str(num + j) for j in range(i)))
        num += i

# 39. Pascal’s triangle
def pascal_triangle(n):
    from math import comb
    for i in range(n):
        print(' '*(n-i), end='')
        for j in range(i+1):
            print(comb(i, j), end=' ')
        print()

# 40. Diamond
def print_diamond(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*(2*i+1))
    for i in range(n-2, -1, -1):
        print(' '*(n-i-1) + '*'*(2*i+1))


---

🧠 Intermediate Logic (41–50)

# 41. Leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# 42. Longest word
def longest_word(sentence):
    return max(sentence.split(), key=len)

# 43. Calculator
def calculator(a, b, op):
    return {'+': a+b, '-': a-b, '*': a*b, '/': a/b}.get(op, "Invalid")

# 44. Guessing game
import random
def guess_game():
    target = random.randint(1, 100)
    guess = -1
    while guess != target:
        guess = int(input("Guess: "))
        print("Too low!" if guess < target else "Too high!" if guess > target else "Correct!")

# 45. Balanced brackets
def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack

# 46. Custom split
def custom_split(s, delimiter=' '):
    result = []
    word = ''
    for char in s:
        if char == delimiter:
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    if word:
        result.append(word)
    return result

# 47. Title case
def to_title_case(s):
    return ' '.join(w[0].upper() + w[1:].lower() if w else '' for w in s.split())

# 48. Random password
import string, random
def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# 49. Transpose matrix
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# 50. Contact book
def contact_book():
    contacts = {}
    while True:
        choice = input("1:Add 2:Find 3:Exit > ")
        if choice == '1':
            name = input("Name: ")
            number = input("Number: ")
            contacts[name] = number
        elif choice == '2':
            name = input("Name: ")
            print(contacts.get(name, "Not found"))
        else:
            break


---

🚀 Bonus Challenges (51–60)

# 51. Fibonacci with memoization
def fib_memo(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# 52. Subarray with 0 sum
def has_zero_sum_subarray(arr):
    cum_sum = 0
    seen = set()
    for num in arr:
        cum_sum += num
        if cum_sum == 0 or cum_sum in seen:
            return True
        seen.add(cum_sum)
    return False

# 53. Pairs with target sum
def pairs_with_sum(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        if target - num in seen:
            pairs.append((num, target - num))
        seen.add(num)
    return pairs

# 54. First non-repeating char
def first_non_repeating(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return None

# 55. Permutations of string
from itertools import permutations
def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

# 56. Longest common prefix
def longest_common_prefix(strs):
    if not strs: return ''
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

# 57. Move zeros to end
def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    return non_zero + [0]*(len(lst)-len(non_zero))

# 58. Majority element (n//2 times)
def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate if nums.count(candidate) > len(nums)//2 else None

# 59. Detect loop in list
def has_loop(arr):
    seen = set()
    for val in arr:
        if val in seen:
            return True
        seen.add(val)
    return False

# 60. Intersection and union of two lists
def intersection_union(lst1, lst2):
    return list(set(lst1) & set(lst2)), list(set(lst1) | set(lst2))


---

✅ Let me know if you want this as a downloadable .py file, categorized Jupyter Notebook, or practice problem sheet with outputs.

