class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        cur, rem = 0, 0
        summ = sum(nums) % p 
        if summ % p == 0:
            return 0

        dic = {0: -1}
        n=len(nums)

        for i, num in enumerate(nums):
            cur = (cur + num) % p
            rem = (cur - summ) % p
            if rem in dic:
                n = min(n, i-dic[rem])
            dic[cur] = i
        return n if n<len(nums)else -1
