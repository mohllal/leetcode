class Solution:
    # O(n * log n) time and O(1) space
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        maximumBars = 0
        for cost in costs:
            if cost > coins:
                break

            coins -= cost
            maximumBars += 1
        
        return maximumBars
