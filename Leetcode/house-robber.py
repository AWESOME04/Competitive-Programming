class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        # memo = [0] * len(nums) - using an array
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
            # if not memo[i] - memo array implementation
                memo[i] = max((dp(i+1), dp(i+2) + nums[i]))
            return memo[i]
        return dp(0)
