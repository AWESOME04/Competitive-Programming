def check_sortability(n, k, p):
    count = 0
    for i in range(n):
        if (p[i] - i - 1) % k != 0:
            count += 1

    if count == 0:
        return 0
    elif count <= 2:
        return 1
    else:
        return -1

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    result = check_sortability(n, k, p)
    print(result)
