class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # hashset = {k: set(k) for k in words}
        # ans = 0
        # n = len(words)

        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         w1, w2 = words[i], words[j]
        #         if not (hashset[w1] & hashset[w2]):
        #             ans = max(ans, len(w1) * len(w2))
        # return ans

        # Optimized Solution
        n = len(words)
        bits = [0] * n
        res = 0

        for ind, word in enumerate(words):
            for ch in word:
                bits[ind] |= 1 << (ord(ch) - ord("a"))

        for i in range(n):
            for j in range(i+1, n):
                if not (bits[i] & bits[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
        
