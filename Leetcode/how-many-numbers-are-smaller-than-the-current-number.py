class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101 
        for num in nums:
            freq[num] += 1

        cum_sum = [0] * 101
        cum_sum[0] = freq[0]
        for i in range(1, 101):
            cum_sum[i] = cum_sum[i - 1] + freq[i]

        result = []
        for num in nums:
            count = cum_sum[num - 1] if num > 0 else 0
            result.append(count)

        return result
