def solve():
    n = int(input())
    for i in range(31, -1, -1):
        if n & (1 << i):
            print((1 << i) - 1)
            return


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()