t = int(input())
ans = []

for _ in range(t):
    count = 0
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
        if arr[i+1] == 0 and arr[i] != 0:
            arr[i] -= 1
            arr[i+1] += 1
            count += 1

    for i in range(n-1):
        count += arr[i]
    ans.append(count)

for val in ans:
    print(val)
