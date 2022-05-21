class Solution:
    # O(n * log n) time and O(1) space
    def thirdMaxLinearithmicTimeAndConstantSpace(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        maximum = nums[0]
        distinct = 1
        
        for num in nums:
            if num != maximum:
                maximum = num
                distinct += 1
            if distinct == 3:
                return maximum

        return nums[0]

    # O(n) time and O(1) space
    def thirdMaxLinearTimeAndConstantSpace(self, nums: List[int]) -> int:
        firstMaximum = None
        for num in nums:
            if firstMaximum is None or num > firstMaximum:
                firstMaximum = num

        secondMaximum = None
        for num in nums:
            if (secondMaximum is None or num > secondMaximum) and (num != firstMaximum):
                secondMaximum = num
        
        thirdMaximum = None
        for num in nums:
            if (thirdMaximum is None or num > thirdMaximum) and (num != firstMaximum and num != secondMaximum):
                thirdMaximum = num
        
        if firstMaximum is not None and secondMaximum is not None and thirdMaximum is not None:
            return thirdMaximum
        else:
            return firstMaximum

    def thirdMax(self, nums: List[int]) -> int:
        return self.thirdMaxLinearTimeAndConstantSpace(nums)