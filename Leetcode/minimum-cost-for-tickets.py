class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        day_values = [1, 7, 30]
        dp[days[0]] = min(costs)

        for i in range(min(days), 366):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = float("inf")
                for j in range(3):
                    dp[i] = min(dp[i], dp[i-day_values[j]] + costs[j])

        return dp[365]
