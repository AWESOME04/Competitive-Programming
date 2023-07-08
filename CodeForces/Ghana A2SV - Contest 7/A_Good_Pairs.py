def asquare():
    n = int(input())
    arr = list(map(int, input().split()))

    pairs = [(arr[i], i+1) for i in range(n)]

    if n == 1:
        print("1 1")
        return

    pairs.sort()

    print(pairs[0][1], pairs[-1][1])


t = int(input())

for _ in range(t):
    asquare()
