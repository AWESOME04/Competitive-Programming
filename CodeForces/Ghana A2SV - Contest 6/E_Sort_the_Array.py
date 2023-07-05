def solve(): 
    n = int(input())
    a = list(map(int, input().split()))
    a = [float("-inf")] + a + [float("inf")]

    start = end = 1
    for i in range(n-1):
        if a[i] > a[i+1]:
            start = i
            break
    for i in range(n, 0, -1):
        if a[i] < a[i-1]:
            end = i
            break

    decreasing = a[start:end+1]
    if (a[start] < a[end+1]) and (a[start-1] < a[end]) and sorted(decreasing) == decreasing[::-1]:
        print("yes")
        print(start, end)
        return
    print("no")

solve()
