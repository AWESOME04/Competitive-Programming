class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force 
        # TC - O(N^2); SP - O(1)

        # n = len(nums)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

        # Optimized Solution using Hashmap 
        # TC - O(N); SC - O(N)

        prevMap = {} # value: index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
