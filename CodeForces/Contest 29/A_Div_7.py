t = int(input())
for _ in range(t):
    n = int(input())

    x = n % 7
    y = 7 - x
    last = n % 10

    if n % 7 == 0:
        pass
    elif last + y < 10:
        n += y
    else:
        n -= x

    print(n)
