class Solution:
    # O(n) time and O(1) space
    def findMaxConsecutiveOnesTwoPointers(self, nums: List[int]) -> int:
        result = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
            else:
                result = max((j - i), result)
                j += 1
                i = j

        return max(result, (j - i))

    # O(n) time and O(1) space
    def findMaxConsecutiveOnesIterative(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                result = max(result, current)
            else:
                current = 0

        return result
    
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return self.findMaxConsecutiveOnesTwoPointers(nums)