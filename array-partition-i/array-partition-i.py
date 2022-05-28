class Solution:
    # O(n * log n) time and O(1) space
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i = len(nums) - 2
        result = 0
        while i >= 0:
            result += nums[i]
            i -= 2
    
        return result