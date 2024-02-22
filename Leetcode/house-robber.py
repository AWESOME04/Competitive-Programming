class Solution:
    def rob(self, nums: List[int]) -> int:
        # memo = {}
        # # memo = [0] * len(nums) - using an array
        # def dp(i):
        #     if i >= len(nums):
        #         return 0
        #     if i not in memo:
        #     # if not memo[i] - memo array implementation
        #         memo[i] = max((dp(i+1), dp(i+2) + nums[i]))
        #     return memo[i]
        # return dp(0)

        # def dp(i):
        #     if i == 0:
        #         return nums[i]
        #     if i == 1:
        #         return max(nums[0],nums[1])
        #     if i not in memo:
        #         memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
        #     return memo[i]
        # memo = {}
        # return dp(len(nums) - 1)

        # Using Bottom Up Approach
        # n = len(nums)
        # dp = [0] * (n+2)
        # for i in range(2, n+2):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i-2])
        # return dp[n+1]

        # Bottom Up with memory optimization
        prev, curr = 0, 0
        for i in range(2, len(nums)+2):
            temp = curr
            curr = max(curr, prev+nums[i-2])
            prev = temp
        return curr
