class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0

        for i in nums:
            if i % 2 == 1:
                prefixSum += 1
            ans += dic[prefixSum-k]
            dic[prefixSum] += 1
        return ans
