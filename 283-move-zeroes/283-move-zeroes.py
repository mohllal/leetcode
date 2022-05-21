class Solution:
    # O(n) time and O(1) space
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1