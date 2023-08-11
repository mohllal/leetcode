class Solution:
    # O(n) time and O(1) space
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                decreasing = False
            
            if nums[i] > nums[i + 1]:
                increasing = False
        
        return increasing or decreasing
        