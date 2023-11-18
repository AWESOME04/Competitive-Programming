def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort(reverse=True)

    if n == 1 and v[0] != 0:
        print("NO")
        return

    for i in range(n-1):
        x = v[i]
        if x == -1:
            continue
        for j in range(i+1, n):
            if v[j] == x-1:
                v[j] = -1
                x -= 1
            if x == 0:
                break
        if x != 0:
            print("NO")
            return

    print("YES")

t = int(input())
for _ in range(t):
    solve()
