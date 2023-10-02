class Solution:
    # O(2^n) time and O(2^n) space or O(n) space if we exclude the result set space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subsetsHelper(nums, prefix, start, powerset):
            powerset.append(prefix[:])
    
            for i in range(start, len(nums)):
                prefix.append(nums[i])
                subsetsHelper(nums, prefix, i + 1, powerset)
                prefix.pop()

        prefix = []
        powerset = []
        start = 0
        subsetsHelper(nums, prefix, start, powerset)
        return powerset