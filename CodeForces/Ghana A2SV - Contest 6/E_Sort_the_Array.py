def solve():
    n = int(input())
    array = list(map(int, input().split()))
    array = [float("-inf")] + array + [float("inf")]

    left = 1
    right = 1
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            left = i
            break
    for i in range(n, 0, -1):
        if array[i] < array[i - 1]:
            right = i
            break

    decreasing_subarray = array[left:right + 1]
    if (array[left] < array[right + 1]) and (array[left - 1] < array[right]) and sorted(decreasing_subarray) == decreasing_subarray[::-1]:
        print("yes")
        print(left, right)
    else:
        print("no")


solve()
