class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        smallest = float('inf')
        for i in prices:
            if i < smallest:
                smallest = i
            else:
                if (i - smallest) > maxProfit:
                    maxProfit = i - smallest

        return maxProfit
