def solve():
    matrix = []
    for _ in range(2):
        row = list(map(int, input().split()))
        matrix.append(row)

    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    if (b > a and d > c and c > a and d > b) or \
       (a > c and b > d and d > c and b > a) or \
       (c > d and a > b and b > d and a > c) or \
       (d > b and c > a and a > b and c > d):
        print("YES")
    else:
        print("NO")

testCase = int(input())
for _ in range(testCase):
    solve()
