class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using bit manipulation - TC: O(); SC: O(1)
        res = 0
        for num in nums:
            res ^= num
        return res
        
