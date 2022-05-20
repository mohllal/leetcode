class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                result = max(result, current)
            else:
                current = 0
        return result