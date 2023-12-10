n = int(input())
number = 0
h = []
a = []

for i in range(n):
    hi, ai = map(int, input().split())
    h.append(hi)
    a.append(ai)

for i in range(n):
    for j in range(n):
        if i != j and (h[i] == a[j]):
            number += 1

print(number)
