class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        Buy = 0
        sell = 1
        profit = 0
        
        while sell < len(prices):
            if prices[sell] > prices[Buy]:
                current_profit= prices[sell] - prices[Buy]
                profit = max(profit,current_profit)
            else:
                Buy = sell
            sell += 1
        return profit



        