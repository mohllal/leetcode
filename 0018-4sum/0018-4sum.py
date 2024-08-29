class Solution:
    # O(n^4) time and O(n^4) space
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        nums.sort()
        
        def searchPair(nums, i, j, quadruplets):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1                

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
    
                searchPair(nums, i, j, quadruplets)
        
        return quadruplets