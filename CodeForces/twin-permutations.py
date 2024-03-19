t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        arr[i] = n + 1 - arr[i]

    print(*arr)
