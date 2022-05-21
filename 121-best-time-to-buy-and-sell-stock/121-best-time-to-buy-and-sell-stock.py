class Solution:
    # O(n ^ 2) time and O(1) space
    def maxProfitQuadraticTimeAndConstantSpace(self, prices: List[int]) -> int:
        result = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                current = prices[j] - prices[i]
                if current > result:
                    result = current
        return result

    # O(n) time and O(1) space
    def maxProfitLinearTimeAndConstantSpace(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                currentProfit = prices[i] - buyPrice
                if currentProfit > profit:
                    profit = currentProfit
        return profit
    
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitLinearTimeAndConstantSpace(prices)