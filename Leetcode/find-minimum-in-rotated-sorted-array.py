class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(N) Solution
        # return min(nums)

        # O(Log N) Solution
        # Since the array is rotated the values on the left side of the mid are greater than the values on the right side of the mid
        # Check if the mid is part of the left shifted portion

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
