n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
diff = [0] * n

for i in range(n):
    diff[i] = A[i] - B[i]

diff.sort()

total = 0
beg = 0
end = n - 1

while end >= beg:
    while beg < end and diff[beg] + diff[end] <= 0:
        beg += 1
    total += max(0, end - beg)
    end -= 1

print(total)