x = int(input())
res = 0

while x != 0:
    if x % 2 == 1:
        res += 1
    x //= 2
print(res)
