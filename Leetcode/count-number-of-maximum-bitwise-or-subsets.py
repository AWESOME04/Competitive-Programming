class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        def backtrack(start, bit_or):
            res.append(bit_or)
            
            for i in range(start, len(nums)):
                backtrack(i + 1, bit_or | nums[i])
        backtrack(0, 0)
        res = Counter(res)
        
        return max(res.values())
