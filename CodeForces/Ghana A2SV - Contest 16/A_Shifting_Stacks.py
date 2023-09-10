t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(n-1):
        if heights[i] < i:
            print("NO")
            break
        heights[i+1] += heights[i] - i
    else:
        if heights[-1] >= n-1:
            print("YES")
        else:
            print("NO")
