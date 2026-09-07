class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        diff = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else: 
                temp = prices[i] - min
                if temp > diff:
                    diff = temp
        
        return diff
