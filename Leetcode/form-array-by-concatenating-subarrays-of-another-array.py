class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        pointer = 0
        groups.reverse()

        while pointer <= len(nums):
            if len(groups) == 0:
                return True
            
            currentGroup = groups[-1]
            if nums[pointer : pointer + len(groups[-1])] == currentGroup:
                pointer += len(currentGroup)
                groups.pop()
            else:
                pointer += 1

        return False
