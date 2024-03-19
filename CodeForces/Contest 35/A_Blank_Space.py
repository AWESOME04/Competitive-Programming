t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(str, input().split("1")))
    print(arr)
    res = 0
    # for val in arr:
    #     res = max(res, len(val))
    # print(res)
    for val in arr:
        print(len(val))

    # count = 1
    # max_count = 1

    # if 0 not in arr:
    #     print(0)
    # else:
    #     for i in range(1, n):
    #         if arr[i] == arr[i-1] == 0:
    #             count += 1
    #         else:
    #             count = 1
    #         max_count = max(count, max_count)
        
    #     print(max_count)
