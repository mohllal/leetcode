class Solution:
    # O(log n) time and O(log n) space
    def binarySearchRecursive(self, left: int, right: int, numbers: List[int], target:int) -> int:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            return self.binarySearchRecursive(left, mid - 1, numbers, target)
        else:
            return self.binarySearchRecursive(mid + 1, right, numbers, target)
    
    # O(log n) time and O(1) space
    def binarySearchIterative(self, left: int, right: int, numbers: List[int], target:int) -> int:
        while left <= right:
            mid = (left + right) // 2
            
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    # O(n * log n) time and O(n * log n) space
    def twoSumLinearithmicTimeAndLinearithmicSpace(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            remaining = target - numbers[i]
            j = self.binarySearchRecursive(i + 1, len(numbers) - 1, numbers, remaining)
            if j != -1:
                return [i + 1, j + 1]

    # O(n) time and O(1) space
    def twoSumLinearTimeAndConstantSpace(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            if (numbers[i] + numbers[j]) == target:
                return [i + 1, j + 1]
            elif (numbers[i] + numbers[j]) > target:
                j -= 1
            else:
                i += 1

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoSumLinearTimeAndConstantSpace(numbers, target)