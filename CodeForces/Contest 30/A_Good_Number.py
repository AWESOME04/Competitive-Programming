n, k = map(int, input().split())

count = 0

for _ in range(n):
    a = input()
    res = 0
    for i in range(k+1):
        if str(i) in a:
            res += 1
    if res == k + 1:
        count += 1

print(count)