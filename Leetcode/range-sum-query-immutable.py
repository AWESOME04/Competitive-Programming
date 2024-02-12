# class NumArray:

#     def __init__(self, nums: List[int]):
#         n = len(nums)
#         self.pre_sum = [0] * n
#         for i in range(n):
#             if i == 0:
#                 self.pre_sum[i] += nums[i]
#             else:
#                 self.pre_sum[i] = self.pre_sum[i-1] + nums[i] 


#     def sumRange(self, left: int, right: int) -> int:
#         if left > 0:
#             return self.pre_sum[right] - self.pre_sum[left - 1]
#         else:
#             return self.pre_sum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix_sum.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        RightSum = self.prefix_sum[right]
        leftSum = self.prefix_sum[left - 1] if left > 0 else 0
        return RightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
