class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Using Prefix Sum
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        prefix, res, dishes_sum = 0, 0, 0

        for i in range(n):
            prefix += satisfaction[i]
            dishes_sum += prefix
            res = max(res, dishes_sum)
        return res
