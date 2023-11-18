t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    result = -1
    for p in range(2, n):
        if arr[p - 2] == arr[p - 1] == arr[p]:
            result = arr[p]
            break

    print(result)


