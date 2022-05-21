# XOR truth table:
# 0, 0 -> 0
# 0, 1 -> 1
# 1, 0 -> 1
# 1, 1 -> 0

class Solution:
    # O(n) time and O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result