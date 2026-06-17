class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = float("inf")
        maxp = 0
        for i in prices:
            if i<minp:
                minp = i
            else:
                profit = i - minp
                maxp = max(maxp,profit)
        return maxp

        