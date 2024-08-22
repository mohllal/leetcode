class Solution:
    # O(n) time and O(1) space
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        next_non_val = 0
        
        while current < len(nums):
            if nums[current] != val:
                nums[next_non_val], nums[current] = nums[current], nums[next_non_val]
                next_non_val += 1

            current += 1

        return next_non_val