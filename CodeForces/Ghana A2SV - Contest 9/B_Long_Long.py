def long():
    n = int(input())
    arr = list(map(int, input().split()))

    max_sum = 0
    pos_sum = 0
    count = 0
    ans = 0

    for x in arr:
        max_sum += abs(x)
        if x == 0 and count == 0:
            continue
        if x <= 0:
            count += 1
        else:
            if count > 0:
                ans += 1
            count = 0
        pos_sum += max(x, 0)

    if count:
        ans += 1

    print(max_sum, ans)


t = int(input())
for _ in range(t):
    long()
