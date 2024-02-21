class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(memo, i):
            if memo[i]:
                return memo[i]
            if i == 0:
                return 0
            memo[i] = float("inf")
            for coin in coins:
                if i - coin >= 0:
                    memo[i] = min(memo[i], dp(memo, i-coin) + 1)
            return memo[i]

        memo = collections.defaultdict(int)
        res = dp(memo, amount)
        return res if res != float("inf") else -1
