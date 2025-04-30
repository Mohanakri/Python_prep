

1. a={'a:',[1,2,3]}

       for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

 2.input into tuple

 n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))

3.passing only one char in string in loop

    s = input()
    print(any(c.isalnum() for c in s))
