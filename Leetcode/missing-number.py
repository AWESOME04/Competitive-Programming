class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      largest = max(nums)
      wholeList = list(range(0, largest+2))

      for i in wholeList:
          if wholeList[i] not in nums:
              return wholeList[i]
