class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")
        l, tot = 0, 0
        for r in range(n):
            tot += nums[r]
            while tot >= target:
                res = min(r - l + 1, res)
                tot -= nums[l]
                l += 1

        if res == float("inf"):
            return 0
        else:
            return res
