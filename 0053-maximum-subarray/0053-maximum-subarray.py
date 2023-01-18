class Solution:
    # O(n) time and O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        current = maximum = float("-inf")

        for num in nums:
            current = max(current, 0) + num
            maximum = max(maximum, current)

        return maximum