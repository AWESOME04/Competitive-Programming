class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        for i in range(0, len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
