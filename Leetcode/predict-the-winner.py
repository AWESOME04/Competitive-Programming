class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = nums.copy()
        n = len(nums)

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])

        return True if dp[-1] >= 0 else False
            
