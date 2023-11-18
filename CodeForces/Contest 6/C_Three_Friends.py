t = int(input())

while t > 0:
    a = list(map(int, input().split()))
    a.sort()
    ans = 2 * (a[2] - a[0] - 2)
    print(max(0, ans))
    t -= 1
