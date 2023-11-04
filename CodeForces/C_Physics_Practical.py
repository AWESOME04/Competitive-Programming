t = int(input())

c = list(map(int, input().split()))

l = 0
r = len(c) - 1

c.sort()
count = 0

while l < r:
    if c[r] - c[l] > 2:
        c.pop(r)
        count += 1
        r -= 1
    else:
        l += 1
print(count)
