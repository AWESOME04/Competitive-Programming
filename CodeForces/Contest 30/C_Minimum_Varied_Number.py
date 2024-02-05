t = int(input())

for _ in range(t):
    s = int(input())
    res = 0

    pow = 1
    for p in range(9, 0, -1):
        if p > s:
            continue
        res += pow * p
        pow *= 10
        s -= p
        
    print(res)