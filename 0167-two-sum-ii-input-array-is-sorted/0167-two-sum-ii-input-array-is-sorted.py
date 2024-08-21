class Solution:
    # O(n^2) time and O(1) space
    def twoSumQuadraticTimeAndConstantSpace(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return -1
    
    # O(n) time and O(1) space
    def twoSumLinearTimeAndConstantSpace(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]

        return -1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoSumLinearTimeAndConstantSpace(numbers, target)