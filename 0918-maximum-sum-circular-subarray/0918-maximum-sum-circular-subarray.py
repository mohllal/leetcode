class Solution:
    # O(n) time and O(1) space
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSoFar = maxEndingHere = float("-inf")
        minSoFar = minEndingHere = float("inf")
        allSum = 0
        
        for num in nums:
            maxEndingHere = max(maxEndingHere, 0) + num
            maxSoFar = max(maxSoFar, maxEndingHere)
            
            minEndingHere = min(minEndingHere, 0) + num
            minSoFar = min(minSoFar, minEndingHere)
            
            allSum += num
        if allSum == minSoFar:
            return maxSoFar
        else:
            return max(maxSoFar, allSum - minSoFar)
