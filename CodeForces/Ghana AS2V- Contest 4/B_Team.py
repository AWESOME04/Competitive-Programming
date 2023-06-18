n = int(input())

count = 0
for _ in range(1, n+1):
    x, y, z = map(int, input().split())
    if x + y + z >= 2:
        count += 1

print(count)
