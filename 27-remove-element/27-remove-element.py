class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        
        while j < len(nums):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1    
            j += 1

        return i
