class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache
        def dp(i, a, l):
            if a >= 2:
                return 0
            if l >= 3:
                return 0
            if i == n:
                return 1

            P = dp(i+1, a, 0)
            L = dp(i+1, a, l+1)
            A = dp(i+1, a+1, 0)

            ans = (P + L + A) % MOD
            return ans

        return dp(0, 0, 0) % MOD
