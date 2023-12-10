for _ in range(int(input())):
    s = input().strip()
    res = s[0] 
    
    for i in range(1, len(s)):
        if i % 2 == 0 or i == len(s) - 1:
            res += s[i]

    print(res)
