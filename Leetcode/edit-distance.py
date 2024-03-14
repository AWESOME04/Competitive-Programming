class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dp(i, j):
            n = len(word1)
            m = len(word2)

            # base cases
            if i >= n:
                return m - j
            if j >= m:
                return n - i
            if word1[i] == word2[j]:
                return dp(i+1, j+1)

            state = (i, j)
            if state in memo:
                return memo[state]
            memo[state] = 1 + min(
                dp(i+1, j), # insert
                dp(i, j+1), # delete
                dp(i+1, j+1) # replace
            )
            return memo[state]
            
        return dp(0, 0)
        
