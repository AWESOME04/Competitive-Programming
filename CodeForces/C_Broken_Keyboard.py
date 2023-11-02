t = int(input())

for _ in range(t):
    s = input().strip() + '#'
    v = []
    
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            i += 2
        else:
            v.append(s[i])
            i += 1

    v.sort()
    
    st = set()
    for i in range(len(v)):
        if i == 0 or v[i] != v[i - 1]:
            st.add(v[i])

    print("".join(sorted(st)))
