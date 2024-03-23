class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}
        n = len(nums)

        for indx in range(n):
            if nums[indx] in hset and abs(indx - hset[nums[indx]]) <= k:
                return True
            hset[nums[indx]] = indx
        return False

        # TC; O(N)
        # SC; O(N)
