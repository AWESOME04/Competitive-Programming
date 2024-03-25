t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    
    if arr[0] == arr[1] + arr[2] or arr[1] == arr[0] + arr[2] or arr[2] == arr[1] + arr[0]:
        print("YES")
    else:
        print("NO")

    # arr.sort()
    # l = 0
    # r = 1
    # if arr[-1] == arr[l] + arr[r]:
    #     print("YES")
    # else:
    #     print("NO")
