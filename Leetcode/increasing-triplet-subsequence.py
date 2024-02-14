class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        f = float("inf")
        s = float("inf")
        l = 0

        while l < n:
            if nums[l] <= f:
                f = nums[l]
                l += 1
            elif nums[l] <= s:
                s = nums[l]
                l += 1
            else:
                return True
        return False
        
