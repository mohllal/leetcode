class Solution:
    # O(n ^ 2) time and O(1) space
    def subarraysDivByKNQuadraticTimeAndConstantSpace(self, nums: List[int], k: int):
        subArraysCount = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                subArraysCount += 1
    
            currentSum = nums[i]
            for j in range(i + 1, len(nums)):
                currentSum += nums[j]
                if currentSum % k == 0:
                    subArraysCount += 1

        return subArraysCount     
    
    # O(n) time and O(k) space
    def subarraysDivByKLinearTimeAndLinearSpace(self, nums: List[int], k: int) -> int:
        remainders: DefaultDict[int, int] = defaultdict(lambda: 0, {0: 1})
        result = 0
        current = 0

        for i in range(len(nums)):
            current += nums[i]
            remainder = current % k

            if remainder < 0:
                remainder += k

            result += remainders[remainder]
            remainders[remainder] += 1
        
        return result

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return self.subarraysDivByKLinearTimeAndLinearSpace(nums, k)

          