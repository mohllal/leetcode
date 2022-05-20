class Solution:
    def findNumbersI(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                result += 1
    
        return result

    def findNumbersII(self, nums: List[int]) -> int:
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
        return self.findNumbersI(nums)