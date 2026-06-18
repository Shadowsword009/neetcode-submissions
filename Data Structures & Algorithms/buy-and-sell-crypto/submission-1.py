class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bbuy,bsell = prices[0],0
        for i in prices:
            if i < bbuy:
                bbuy = i
            if i-bbuy > bsell:
                bsell = i - bbuy
        return bsell