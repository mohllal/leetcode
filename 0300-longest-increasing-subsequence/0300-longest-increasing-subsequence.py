class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.lengthOfLISQuadraticTimeAndLinearSpace(nums)

    # O(n^2) time and O(n) space
    def lengthOfLISQuadraticTimeAndLinearSpace(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        
        maximum = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

            maximum = max(maximum, lis[i])

        return maximum