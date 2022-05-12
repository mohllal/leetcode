# XOR truth table:
# 0, 0 -> 0
# 0, 1 -> 1
# 1, 0 -> 1
# 1, 1 -> 0

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result