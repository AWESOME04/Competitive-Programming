class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))
        l, r = 0, len(nums) - 1

        while l < r:
            m = (r+l) // 2
            if nums[m] >= nums[m+1]:
                r = m
            else:
                l = m + 1

        return l
