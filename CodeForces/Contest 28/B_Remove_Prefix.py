t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * (n + 1)
    res = 0

    for i in range(n):
        b[a[i]] += 1

    for i in range(n):
        if b[a[i]] > 1:
            b[a[i]] -= 1
            res = i + 1

    print(res)
