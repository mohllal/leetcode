class Solution:
    # O(n * logn) time and O(n) space
    def findUnsortedSubarrayLogLinearTimeAndLinearSpace(self, nums: List[int]) -> int:
        sorted_nums = list(sorted(nums))
        
        start = None
        end = None
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                if start is None:
                    start = i
                    end = i
                else:
                    end = i

        return (end - start) + 1 if start is not None else 0
    
    # O(n) time and O(1) space
    def findUnsortedSubarrayLinearTimeAndConstantSpace(self, nums: List[int]) -> int:
        def findUnsortedSubarrayIndices(nums: List[int]) -> Tuple[Optional[int], Optional[int]]:
            left = 0
            while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
                left += 1
                
            if left == len(nums) - 1:
                return None, None
            
            right = len(nums) - 1
            while right > 0 and nums[right] >= nums[right - 1]:
                right -= 1
            
            return left, right
        
        def findSubarrayMinimumAndMaximum(nums: List[int], start: int, end: int) -> Tuple[int, int]:
            minimum = float("inf")
            maximum = float("-inf")
            for i in range(start, end + 1):
                minimum = min(minimum, nums[i])
                maximum = max(maximum, nums[i])
            
            return minimum, maximum
        
        start, end = findUnsortedSubarrayIndices(nums)
        
        if start is None and end is None:
            return 0
    
        minimum, maximum = findSubarrayMinimumAndMaximum(nums, start, end)
        
        # expand the subarray to the left to include any element before the subarray
        # which is smaller than the minimum element of the unsorted subarray
        temp = start - 1
        while temp >= 0:
            if nums[temp] > minimum:
                start = temp
            temp -= 1
        
        # expand the subarray to the right to include any element after the subarray
        # which is larger than the maximum element of the unsorted subarray
        temp = end + 1
        while temp <= len(nums) - 1:
            if nums[temp] < maximum:
                end = temp
            temp += 1
            
        return (end - start) + 1

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        return self.findUnsortedSubarrayLinearTimeAndConstantSpace(nums)