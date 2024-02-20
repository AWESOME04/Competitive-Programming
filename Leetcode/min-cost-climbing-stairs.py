class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        memo = {}

        # for i in range(len(cost)-3, -1, -1):
        #     cost[i] += min(cost[i+1], cost[i+2])
        # return min(cost[0], cost[1])

        def dp(i):
            if i < 2:
                return cost[i]
            if i not in memo:
                memo[i] = min(dp(i-1) + cost[i], dp(i-2) + cost[i])
            return memo[i]
        return dp(len(cost)-1)


        
