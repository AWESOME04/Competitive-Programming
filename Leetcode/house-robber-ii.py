class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i, flag):
            if len(nums) == 1:
                return nums[0]
            if flag:
                arr = nums[1:]
            else:
                arr = nums[:-1]
            if i > len(arr) -1:
                return 0
            if (i, flag) in memo:
                return memo[(i, flag)]
            result = max(dp(i+1, flag), arr[i]+dp(i+2, flag))
            memo[(i, flag)] = result
            return result
        return max(dp(0, True), dp(0, False))
