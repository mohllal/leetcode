class Solution:
    # O(n) time and O(1) space
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1

        return nums
