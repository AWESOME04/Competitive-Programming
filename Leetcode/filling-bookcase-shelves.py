class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache
        def dp(i):
            if i == len(books):
                return 0
            rw, rh = 0, 0
            ans = float("inf")

            for i in range(i, len(books)):
                curr_w, curr_h = books[i]
                rw = curr_w + rw
                if rw <= shelfWidth:
                    rh = max(curr_h, rh)
                    ans = min(ans, rh + dp(i + 1))

            return ans
        return dp(0)
