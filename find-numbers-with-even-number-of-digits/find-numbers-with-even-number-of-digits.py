class Solution:
    # O(n ^ 2) time and O(1) space
    def findNumbersQuadraticTimeAndConstantSpace1(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
    
        return result

    # O(n ^ 2) time and O(1) space
    def findNumberQuadraticTimeAndConstantSpace2(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            digits = 0
            while num != 0:
                num //= 10
                digits += 1
    
            if digits % 2 == 0:
                result += 1
    
        return result

    def findNumbers(self, nums: List[int]) -> int:
        return self.findNumbersQuadraticTimeAndConstantSpace1(nums)