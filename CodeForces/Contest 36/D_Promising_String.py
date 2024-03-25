t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    prefix= [0] * (n)
    for i in range(n):
        if s[i] == "+":
            prefix[i] = prefix[i-1] + 1
        else:
            prefix[i] = prefix[i-1] - 1
    prefix.insert(0, 0)

    for i in range(len(prefix)):
        for j in range(i+1, len(prefix)):
            if prefix[i] >= prefix[j] and (prefix[i] - prefix[j]) % 3 == 0:
                ans += 1
    print(ans)
