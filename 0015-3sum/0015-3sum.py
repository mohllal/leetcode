class Solution:
    # O(n^2) time and O(n) space
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triples = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                
                if current < 0:
                    j += 1
                elif current > 0:
                    k -= 1
                else:
                    triples.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
            
        return triples