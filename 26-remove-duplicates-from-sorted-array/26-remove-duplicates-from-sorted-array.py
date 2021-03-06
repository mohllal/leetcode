class Solution:
    # O(n) time and O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0

        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1

        return i + 1