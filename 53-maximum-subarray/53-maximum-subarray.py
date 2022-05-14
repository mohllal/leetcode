class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > current and current < 0:
                current = nums[i]
            else:
                current += nums[i]
                
            if current > maximum:
                maximum = current

        return maximum