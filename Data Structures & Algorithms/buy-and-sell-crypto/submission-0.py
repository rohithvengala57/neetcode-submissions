class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0 
        j = 1
        Mp = 0
        while j < len(prices):
            if prices[j] - prices[i] < 0:
                i = j
                j+=1
            else:
                Mp = max(Mp, prices[j] - prices[i])
                j+=1
        return Mp