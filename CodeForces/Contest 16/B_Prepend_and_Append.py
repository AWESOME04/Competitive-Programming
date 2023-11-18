t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    shortest = n
    l = 0
    r = n-1

    while l < r:
        if s[l] != s[r]:
            l += 1
            r -= 1
            shortest -= 2
        else:
            break

    print(shortest)
