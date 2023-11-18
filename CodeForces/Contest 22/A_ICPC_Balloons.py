t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    for i in range(len(s)):
        score = 0
        s_set = set(s)
        if len(s_set) == len(s):
            score = len(s) * 2
        else:
            dup = len(s) - len(s_set)
            score = len(s) * 2 - dup
    print(score)

