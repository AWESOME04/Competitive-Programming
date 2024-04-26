class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for i in range(len(nums)): - O(n^2) and O(1)
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        # Using prefix sum - O(n) and O(n)
        # n = len(nums)
        # prefix = [0] * (n + 1)
        # suffix = [0] * (n + 1)

        # for i in range(1, n+1):
        #     prefix[i] = prefix[i-1] + nums[i-1]

        # for i in range(n-1, -1, -1):
        #     suffix[i] = suffix[i+1] + nums[i]

        # ans = -1
        # for i in range(1, len(prefix)): 
        #     if prefix[i-1] == suffix[i]:
        #         ans = i - 1
        #         break 
        # return ans

        # Optimal Solution - O(n) and O(1)
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1
