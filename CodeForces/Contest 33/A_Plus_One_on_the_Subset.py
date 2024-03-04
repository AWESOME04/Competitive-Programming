def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        maxx = 0
        minn = 10**9 + 7
        numbers = list(map(int, input().split()))
        for x in numbers:
            minn = min(minn, x)
            maxx = max(maxx, x)

        print(maxx - minn)

if __name__ == "__main__":
    main()
