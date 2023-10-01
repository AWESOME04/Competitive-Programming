t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    res = 0

    l, h = 0, (a+b) // 4

    while l <= h:
        m = (l+h) // 2

        if a + b >= 4*m and a >= m and b >= m:
            res = m
            l = m + 1
        else:
            h = m - 1

    print(res)
