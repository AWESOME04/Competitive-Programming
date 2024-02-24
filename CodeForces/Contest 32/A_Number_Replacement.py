t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = input().strip()

    flag = True
    hash1 = {}
    hash2 = {}
    
    for i in range(n):
        if arr[i] not in hash1:
            hash2[arr[i]] = s[i]
        elif hash2[arr[i]] != s[i]:
            flag = False
        hash1[arr[i]] = hash1.get(arr[i], 0) + 1
    if flag:
        print("YES")
    else:
        print("NO")
