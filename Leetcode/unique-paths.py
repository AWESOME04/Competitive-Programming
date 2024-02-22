class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def dp(r, c, rows, cols, cache):
        #     if r == rows or c == cols:
        #         return 0
        #     if r == rows - 1 or c == cols -1:
        #         return 1
        #     if cache[r][c] > 0:
        #         return cache[r][c]

        #     cache[r][c] =  (dp(r+1, c, rows, cols, cache) + dp(r, c+1, rows, cols, cache))
        #     return cache[r][c]
        
        # return dp(0, 0, m, n, [[0] * n for i in range(m)])

        # Using Bottom Up Approach
        dp = [[0]* n for _ in range(m)]

        for i in range(m):
            dp[i][n-1] = 1
        
        for j in range(n):
            dp[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]
