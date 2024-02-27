class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        if n < 2:
            return 0
        buy = -prices[0]
        profit = 0
        for i in range(1, n):
            buy = max(buy, profit - prices[i])
            profit = max(profit, buy + prices[i] - fee)
        return profit
