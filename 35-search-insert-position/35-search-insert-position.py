def binarySearch(low, high, nums: List[int], target: int):
    if high < low:
        return low

    mid = (high + low) // 2
    if nums[mid] > target:
        return binarySearch(low, mid - 1,  nums, target)
    elif nums[mid] < target:
        return binarySearch(mid + 1, high, nums, target)
    else:
        return mid

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binarySearch(0, len(nums) - 1, nums, target)