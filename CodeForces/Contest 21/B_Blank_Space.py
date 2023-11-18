for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    blank = 1
    max_blank = 1

    if 0 not in arr:
        print(0)
    else:
        for i in range(1, n):
            if arr[i] == arr[i-1] == 0:
                blank += 1
            else:
                blank = 1
            max_blank = max(blank, max_blank)
        
        print(max_blank)
