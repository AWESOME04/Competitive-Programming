t = int(input())

for _ in range(t):
    n = int(input())
    poly = list(map(int, input().split()))

    # create two pointers
    left_ptr = 0
    right_ptr = n - 1

    solution = []
    while left_ptr <= right_ptr:
        solution.append(poly[left_ptr])
        if left_ptr == right_ptr:
            break
        solution.append(poly[right_ptr])
        left_ptr += 1
        right_ptr -= 1
    print(*solution)