class Solution:
    # O(n) time and O(1) space
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = float("-inf")
        
        current = 0
        for i in range(0, len(nums)):
            current += nums[i]
            
            if i >= k - 1:
                maximum = max(maximum, current / k)
                current -= nums[i - (k - 1)]
        
        return maximum