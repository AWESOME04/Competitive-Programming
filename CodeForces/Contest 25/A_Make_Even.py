t = int(input())

for _ in range(t):
    s = input()
    n = len(s)
    ops = -1

    if int(s[-1]) % 2 == 0:
        ops = 0
    elif int(s[0]) % 2 == 0:
        ops = 1
    else:
        for i in range(1, n - 1):
            if int(s[i]) % 2 == 0:
                ops = 2
                break

    print(ops)
