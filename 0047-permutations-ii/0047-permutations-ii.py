class Solution:
    # O(Σk=1, n P(n,k)) time and O(n*n!) space
    # P(n,k) = n!/(n-k)!
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permuteHelper(nums, prefix, visited, premutations):
            if len(prefix) == len(nums):
                premutations.append(prefix[:])
                return
            
            lookup = set()
            for i in range(len(nums)):
                if not visited[i] and nums[i] not in lookup:
                    visited[i] = True
                    prefix.append(nums[i])
                    permuteHelper(nums, prefix, visited, premutations)
                    visited[i] = False
                    prefix.pop()
                    
                    lookup.add(nums[i])
        
        premutations = []
        prefix = []
        visited = [False] * len(nums)
        permuteHelper(nums, prefix, visited, premutations)
        return premutations