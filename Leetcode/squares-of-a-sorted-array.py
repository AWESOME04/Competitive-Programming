class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = abs(nums[i]) * abs(nums[i])

        # return sorted(nums)
        return sorted([abs(num) * abs(num) for num in nums])
