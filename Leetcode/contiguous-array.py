class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        n = len(nums)
        count = 0
        ans = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            if count in hashmap:
                ans = max(ans, i-hashmap[count])
            else:
                hashmap[count] = i
        return ans
