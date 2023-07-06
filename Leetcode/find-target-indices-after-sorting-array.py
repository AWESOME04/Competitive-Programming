class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        lessThan = sum(num < target for num in nums)
        indices = [i for i in range(lessThan, lessThan + count)]
        return indices
