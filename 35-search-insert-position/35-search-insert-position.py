class Solution:
    # O(log n) and O(1) space
    def binarySearch(self, low, high, nums: List[int], target: int):
        if high < low:
            return low

        mid = (high + low) // 2

        if nums[mid] > target:
            return self.binarySearch(low, mid - 1,  nums, target)
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, high, nums, target)
        else:
            return mid

    # O(log n) and O(1) space
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(0, len(nums) - 1, nums, target)