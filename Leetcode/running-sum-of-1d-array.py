class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_sum = [0] * n
        for i in range(n):
            if i == 0:
                pre_sum[i] += nums[i]
            else:
                pre_sum[i] = pre_sum[i-1] + nums[i] 

        return pre_sum
