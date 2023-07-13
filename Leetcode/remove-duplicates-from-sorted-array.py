class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        return i + 1


"""
Alrternative: Brute Force Approach
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = [nums[0]]  #assume nums[0] is unique
        count = 1  

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                k.append(nums[i])
                count += 1

        for i in range(count):
            nums[i] = k[i]

        return count
"""

