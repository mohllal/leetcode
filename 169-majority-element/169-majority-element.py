class Solution:
    # O(n ^ 2) time and O(1) space
    def majorityElementQuadraticTimeAndConstantSpace(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            current = nums[i]
            count = 0
            for j in range(len(nums)):
                if current == nums[j]:
                    count += 1
                if count > len(nums) // 2:
                    return nums[j]
    
    # O(n * log n) time and O(1) space
    def majorityElementLinearithmicTimeAndConstantSpace(self, nums: List[int]):
        nums.sort()
        count, temp = 1, nums[0]
        for i in range(1, len(nums)):
            if temp == nums[i]:
                count += 1
            else:
                count = 1;
                temp = nums[i]
            if count > len(nums) // 2:
                return nums[i]

    # O(n) time and O(1) space
    def majorityElementLinearTimeAndConstantSpace(self, nums: List[int]):
        candidate, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
            if candidate == nums[i]:
                count += 1
            else:
                count -= 1
        return candidate
    
    def majorityElement(self, nums: List[int]):
        return self.majorityElementLinearTimeAndConstantSpace(nums)