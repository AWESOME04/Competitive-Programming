MOD = int(10**9 + 7)

def main():
    s = input()

    f = 0
    for i in s:
        if i == 'm' or i == 'w':
            print(0)
            return

    dp = [0] * (len(s)+1)
    dp[0] = dp[1] = 1

    for i in range(2, len(s)+1):
        if s[i - 2:i] == "nn" or s[i - 2:i] == "uu":
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]

    print(dp[-1]% MOD)

if __name__ == "__main__":
    main()
