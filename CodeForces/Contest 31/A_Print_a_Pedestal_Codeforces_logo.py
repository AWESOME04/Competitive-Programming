t = int(input())

for _ in range(t):
    n = int(input())
    if n % 3 == 0:
        h1 = n // 3 + 1
        h2 = n // 3
        h3 = n // 3 - 1
    elif n % 3 == 1:
        h1 = n // 3 + 2
        h2 = n // 3
        h3 = n // 3 - 1
    else:
        h1 = n // 3 + 2
        h2 = n // 3 + 1
        h3 = n // 3 - 1
        
    print(h2, h1, h3)