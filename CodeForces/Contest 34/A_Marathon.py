t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    count = 0
    n = len(arr)
    
    timur = arr[0]
    for i in range(1, n):
        if arr[i] > timur:
            count += 1
    print(count)