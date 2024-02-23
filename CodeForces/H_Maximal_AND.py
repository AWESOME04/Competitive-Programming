t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(30, -1, -1):
        p = 0
        x = pow(2, i)
        for j in range(n):
           if (a[j] & x) == 0:
                p +=  1
        if p <= k:
            k -= p
            ans += x
    print(ans)
