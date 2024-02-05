class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        n = len(nums)

        # Brute force Solution
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if i < j and nums[i] + nums[j] < target:
        #             pairs += 1
        # return pairs


        # Two pointers
        nums.sort()

        l, r = 0, n - 1

        while l < r:
            if nums[l] + nums[r] < target:
                pairs += r - l
                l += 1
            else:
                r -= 1
        return pairs
