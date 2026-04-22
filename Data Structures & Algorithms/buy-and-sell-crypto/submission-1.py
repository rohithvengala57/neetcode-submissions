class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = 0
        maxProfit = 0
        for i,val in enumerate(prices):
            if prices[i] < prices[minbuy]:
                minbuy = i
            maxProfit = max(val - prices[minbuy], maxProfit)
        return maxProfit