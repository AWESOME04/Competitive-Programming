t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n

    for i in range(n - 1, -1, -1):
        ans[i] = a[i]
        in_index = i + a[i]
        
        if in_index < n:
            ans[i] += ans[in_index]
    res = max(ans)
    print(res)
