class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prevSum, curSum, res, zeroFound = 0, 0, 0, False
        for i in range(len(nums)):
            if nums[i] == 1:
                curSum += 1
            if nums[i] == 0:
                res = max(prevSum + curSum, res)
                prevSum = curSum
                curSum = 0
                zeroFound = True
        return max(prevSum + curSum, res) - 1 if not zeroFound else max(prevSum + curSum, res)
        
