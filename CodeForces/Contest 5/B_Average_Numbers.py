n = int(input())

ints = list(map(int, input().split()))

total = sum(ints)

indices = []

for i in range(n):
    if (total - ints[i] )/ (n-1) == ints[i]:
        indices.append(i+1)

print(len(indices))
print(*indices)
