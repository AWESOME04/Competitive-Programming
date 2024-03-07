class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        def inbound(i, j):
            if 0<=i<n and 0<=j<m:
                return dp[i][j]
            return 0

        dp = [[0 for i in range(m)]for j in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = inbound(i+1, j+1) + 1
                else:
                    dp[i][j] = max(inbound(i+1, j), inbound(i, j+1))
        return dp[0][0]
