class Solution:
    # O(n ^ 2) time and O(1) space
    def pivotIndexQuadraticTimeAndConstantSpace(self, nums: List[int]) -> int:
        leftSum = 0
        for i in range(0, len(nums)):
            rightSum = 0
            for j in range(i + 1, len(nums)):
                rightSum += nums[j]
            
            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        
        return -1 if leftSum != 0 else len(nums) - 1
    
    # O(n) time and O(n) space
    def pivotIndexLinearTimeAndLinearSpace(self, nums: List[int]) -> int:
        sums = [0]
        current = 0
        for i in range(0, len(nums)):
            current += nums[i]
            sums.append(current)

        for i in range(1, len(sums)):
            left = sums[i - 1]
            right = sums[-1] - sums[i]
            
            if left == right:
                return i - 1

        return -1
    
    def pivotIndex(self, nums: List[int]) -> int:
        return self.pivotIndexLinearTimeAndLinearSpace(nums)