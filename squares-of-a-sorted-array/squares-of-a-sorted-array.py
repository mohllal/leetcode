class Solution:
    # O(n * log n) time and O(n) space
    def sortedSquaresLinearithmicTimeAndLinearSpace(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.append(num ** 2)
        result.sort()
        return result
    
    # O(n) time and O(n) space
    def sortedSquaresLinearTimeAndLinearSpace(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        i = 0
        j = len(nums) - 1
        k = len(nums) - 1

        while i <= j:
            if abs(nums[j]) > abs(nums[i]):
                result[k] = nums[j] ** 2
                j -= 1
            else:
                result[k] = nums[i] ** 2
                i += 1
            k -= 1

        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return self.sortedSquaresLinearTimeAndLinearSpace(nums)