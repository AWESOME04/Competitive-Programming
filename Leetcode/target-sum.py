class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, res):
            if i == len(nums):
                return res == target
            if (i, res) not in memo:
                memo[(i, res)] = dp((i+1), res+nums[i]) + dp((i+1), res-nums[i]) 
            return memo[(i, res)]
        return dp(0, 0)
