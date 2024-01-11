class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        res = []

        while i < n:
            curr = nums[i]
            if curr - 1 < n and curr - 1 != i and curr != nums[curr - 1]:
                nums[i], nums[curr - 1] = nums[curr - 1], nums[i]
            else:
                i += 1
        
        for j in range(n):
            if nums[j] != j + 1:
                res.append(j + 1)
        
        return res
