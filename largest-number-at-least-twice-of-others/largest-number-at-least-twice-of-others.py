class Solution:
    # O(n) time and O(1) space
    def dominantIndex(self, nums: List[int]) -> int:
        largest = nums[0]
        index = 0
        for i in range(0, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                index = i

        for num in nums:
            if num != largest and largest < num * 2:
                return -1

        return index