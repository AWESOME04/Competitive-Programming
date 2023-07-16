t = int(input())

for _ in range(t):
    n = int(input())
    polycarp = list(map(int, input().split()))

    left, right = 0, n - 1

    answer = []
    while left <= right:
        answer.append(polycarp[left])
        if left == right:
            break
        answer.append(polycarp[right])
        left += 1
        right -= 1
    print(*answer)
