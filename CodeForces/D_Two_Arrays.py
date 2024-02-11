t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    for i in range(n):
        if b[i] - a[i] > 1 or a[i] > b[i]:
            print("NO")
            break
    else:
        print("YES")
