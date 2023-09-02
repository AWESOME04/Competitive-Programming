n, q = list(map(int, input().split()))

p = list(map(int, input().split()))

p.sort()

prefix_sum = [0] * (n + 1)

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + p[i-1]

for _ in range(q):
    x, y = list(map(int, input().split()))

    res1 = prefix_sum[n - x + y]

    res2 = prefix_sum[n - x]

    result =  res1 - res2

    print(result)


