n, m = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

res = 0
for i in range(n):
    if t[i]:
        res += a[i]
        a[i] = 0

cs = [0] * (n + 1)
for i in range(1, n + 1):
    cs[i] = a[i - 1] + cs[i - 1]

tmp = 0
for i in range(n, m - 1, -1):
    tmp = max(tmp, cs[i] - cs[i - m])

print(res + tmp)
