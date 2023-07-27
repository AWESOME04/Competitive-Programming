class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()

        for num in nums:
            distinct.add(num)
            distinct.add(int(str(num)[::-1]))
        return len(distinct)
