setA, n = set(map(int, input().split())), int(input())
strict = True

for _ in range(n):
    setB = set(map(int, input().split()))
    if not setB.issubset(setA) or len(setB) >= len(setA):
        strict = False
        break
    
print(strict)
