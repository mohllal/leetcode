class Solution:
    # O(n) time and O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        next_non_duplicate = 1
        
        while current < len(nums):
            if nums[next_non_duplicate - 1] != nums[current]:
                nums[next_non_duplicate], nums[current] = nums[current], nums[next_non_duplicate]
                next_non_duplicate += 1
                
            current += 1
            
        return next_non_duplicate