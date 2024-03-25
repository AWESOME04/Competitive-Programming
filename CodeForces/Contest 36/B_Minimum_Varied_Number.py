def solve():
    nums = int(input())
    ans = []

    for i in range(9, 0, -1):
        if nums <= i:
            break
        nums -= i
        ans.append(i)

    ans.append(nums)
    ans = ans[::-1]
    print(''.join(map(str, ans)))

t = int(input())
for _ in range(t):
    solve()