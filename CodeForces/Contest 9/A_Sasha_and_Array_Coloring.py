for _ in range(int(input())):
    n = int(input()) - 1
    arr = list(map(int, input().split()))
    arr.sort()

    l = 0
    r = 0

    while l <= n:
        r += arr[n] - arr[l]
        l += 1
        n -= 1

    print(r)
