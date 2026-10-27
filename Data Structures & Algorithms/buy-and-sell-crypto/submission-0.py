class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(1+i, len(prices)):
              sell = prices[j]
            
              profit = max (profit, (prices[j] - prices[i]))

        return profit
            
        