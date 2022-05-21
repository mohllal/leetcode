class Solution:
    # O(n) time and O(n) space - excluding the result list 
    def findDisappearedNumbersLinearTimeAndLinearSpace(self, nums: List[int]) -> List[int]:
        hashTable = {}
        for num in nums:
            hashTable[num] = True
        
        result = []
        for i in range(1, len(nums) + 1):
            if i not in hashTable:
                result.append(i)
        return result

    # O(n * log n) time and O(1) space - excluding the result list 
    def findDisappearedNumbersLinearithmicTimeAndConstantSpace(self, nums: List[int]) -> List[int]:
        nums.sort()

        result = []
        prev = None

        n = len(nums)
        i = 0
        j = 1
        while i < n:
            if nums[i] == prev:
                i += 1
            elif nums[i] == j:
                j += 1
                prev = nums[i]
                i += 1
    
            elif nums[i] != j:
                result.append(j)
                if j + 1 <= n:
                    j += 1

        while j <= n:
            result.append(j)
            j += 1

        return result

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return self.findDisappearedNumbersLinearithmicTimeAndConstantSpace(nums)