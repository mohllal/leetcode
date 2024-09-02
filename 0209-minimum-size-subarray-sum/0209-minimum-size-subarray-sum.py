class Solution:
    # O(n) time and O(1) space
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_length = float("inf")
        
        window_sum = 0
        window_start = 0
        for i in range(len(nums)):    
            window_sum += nums[i]
            
            while window_sum >= target:
                minimum_length = min(minimum_length, (i - window_start + 1))
                window_sum -= nums[window_start]
                window_start += 1
        
        return 0 if minimum_length == float("inf") else minimum_length