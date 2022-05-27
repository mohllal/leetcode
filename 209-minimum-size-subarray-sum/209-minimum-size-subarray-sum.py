class Solution:
    # O(n ^ 2) time and O(1) space
    def minSubArrayLenQuadraticTimeAndConstantSpace(self, target: int, nums: List[int]) -> int:
        result = None

        for i in range(0, len(nums)):
            current = 0
            for j in range(i, len(nums)):
                current += nums[j]
                if current >= target:
                    if result is None:
                        result = j - i + 1
                    else:
                        result = min(result, j - i + 1)
                    break
        return result if result is not None else 0

    # O(n) time and O(1) space
    def minSubArrayLenLinearTimeAndConstantSpace(self, target: int, nums: List[int]) -> int:
        result = None
        current = 0
        j = 0
        
        for i in range(0, len(nums)):
            if i > 0:
                current -= nums[i - 1]

            while j < len(nums):
                if current >= target:
                    break
                current += nums[j]
                j += 1

            if current >= target and result is None:
                result = j - i
            elif current >= target and result is not None:
                result = min(result, j - i)

        return result if result is not None else 0

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.minSubArrayLenLinearTimeAndConstantSpace(target, nums)