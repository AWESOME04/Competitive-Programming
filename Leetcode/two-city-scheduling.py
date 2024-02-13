class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        - Sort the costs based on the absolute difference
        - The smaller the cost, the higher the priority using Greedy
        - 1st half - City A
        - 2nd half - City B
        """
        costs.sort(key=lambda x: x[0] - x[1])
        res = 0 
        n = len(costs) // 2

        for i in range(n):
            res += costs[i][0] + costs[i+n][1]
        return res
