class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #   largest = max(nums)
        #   wholeList = list(range(0, largest+2))

        #   for i in wholeList:
        #       if wholeList[i] not in nums:
        #           return wholeList[i]

        # ideal_array = []
        # for i in range(len(nums) + 1):
        #     ideal_array.append(i)
        
        # for num in ideal_array:
        #     if num not in nums:
        #         return num
        # return 0

        # Using Cyclic Sort
        n = len(nums)
        i = 0 

        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != i:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for idx in range(n):
            if nums[idx] != idx:
                return idx

        return n

    
