class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        combination = (combinations(nums, r) for r in range(2, len(nums) + 1))
        for arr in chain.from_iterable(combination):
            nonDecreasing = all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))
            if nonDecreasing:
                result.add(arr)

        return result
