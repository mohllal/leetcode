class Solution:
    def maxProfitNaive(self, prices: List[int]) -> int:
        result = 0
        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                current = prices[j] - prices[i]
                if current > result:
                    result = current

        return result

    def maxProfit(self, prices: List[int]) -> int:
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