class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (len(nums)+1)

        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        hashmap = dict()
        count = 0

        for i in range(len(prefix_sum)):
            if prefix_sum[i] % k in hashmap:
                count += hashmap.get(prefix_sum[i] % k)
            hashmap[prefix_sum[i] % k] = hashmap.get(prefix_sum[i] % k, 0) + 1

        return count

