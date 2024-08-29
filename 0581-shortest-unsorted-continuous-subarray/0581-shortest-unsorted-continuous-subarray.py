class Solution:
    # O(n * logn) time and O(n) space
    def findUnsortedSubarray(self, nums: List[int]) -> int:
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