class Solution:
    # O(n ^ 2) time and O(1) space
    def twoSumQuadraticTimeAndConstantSpace(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    return [i, j]

    # O(n) time and O(n) space
    def twoSumLinearTimeAndLinearSpace(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashTable:
                return [i, hashTable[complement]]
            hashTable[nums[i]] = i

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumLinearTimeAndLinearSpace(nums, target)