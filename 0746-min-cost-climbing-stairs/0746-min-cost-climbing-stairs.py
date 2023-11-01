class Solution:
    # O(n) time and O(n) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCostClimbingStairsHelper(index, cost, memo):
            if index >= len(cost):
                return 0
            
            if index in memo:
                return memo[index]
            
            memo[index] = min(
                cost[index] + minCostClimbingStairsHelper(index + 1, cost, memo),
                cost[index] + minCostClimbingStairsHelper(index + 2, cost, memo)
            )
            return memo[index]
        
        memo = {}
        startAtZeroIndex = minCostClimbingStairsHelper(0, cost, memo)
        startAtOneIndex = minCostClimbingStairsHelper(1, cost, memo)

        return min(startAtZeroIndex, startAtOneIndex)
        