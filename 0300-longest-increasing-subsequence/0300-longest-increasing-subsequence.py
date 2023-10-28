class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLISQuadraticTimeAndLinearSpace(nums)

    # O(n^2) time and O(n) space
    def lengthOfLISQuadraticTimeAndLinearSpace(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        
        globalMaximum = 0
        for i in range(len(nums)):
            localMaximum = 0
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    localMaximum = max(lis[j], localMaximum)
            
            lis[i] = 1 + localMaximum
            globalMaximum = max(globalMaximum, lis[i])

        return globalMaximum