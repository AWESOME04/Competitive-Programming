class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # n = len(nums)

        # if n < 3:
        #     return False

        # for i in range(n):
        #     j = i + 1
        #     k = n - 1

        #     while j < k:
        #         if nums[i] < nums[k] < nums[j] and i < j < k:
        #             return True

        #         j += 1
        #         k -= 1

        # return False

        # Monotonically decreasing stack approach
        n = len(nums)
        stack = []
        minn = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, minn])
            minn = min(minn, n)
        return False
