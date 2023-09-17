class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) solution
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]

        # Using Binary Search
        l, r = 1, len(nums) - 1 
        while l < r:
            mid = l + (r - l) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                r = mid
            else:
                l = mid + 1
        
        return l
