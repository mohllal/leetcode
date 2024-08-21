class Solution:
    # O(n) time and O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0
        last_non_duplicate = 0
        
        while current < len(nums):
            if nums[last_non_duplicate] != nums[current]:
                last_non_duplicate += 1
                nums[last_non_duplicate], nums[current] = nums[current], nums[last_non_duplicate]
                
            current += 1
            
        return last_non_duplicate + 1