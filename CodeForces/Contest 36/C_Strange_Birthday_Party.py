t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    c = list(map(int, input().split()))

    k.sort(reverse=True)
    j = 1
    res = 0
    for i in range(n):
        if k[i] >= j:
            res += c[j-1]
            j += 1
        else:
            res += c[k[i] - 1]

    print(res)
