n = int(input())
arr = list(map(int, input().split()))

length = 1
max_length = 1

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        length += 1
        max_length = max(max_length, length)
    else:
        length = 1

print(max_length)
