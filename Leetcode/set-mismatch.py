class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        res = []

        while i < n:
            correct_position = nums[i] - 1
            if nums[i] != nums[correct_position]:
                nums[i], nums[correct_position] = nums[correct_position], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(nums[i])
                res.append(i + 1)
        return res
