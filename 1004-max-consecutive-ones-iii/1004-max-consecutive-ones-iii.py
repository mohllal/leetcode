class Solution:
    # O(n) time and O(1) space
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest_length = 0
        
        window_start = 0
        window_counter = Counter()
        for window_end in range(len(nums)):
            window_end_elem = nums[window_end]
            window_counter[window_end_elem] += 1

            while (window_end - window_start + 1) - window_counter[1] > k:
                window_start_elem = nums[window_start]
                window_counter[window_start_elem] -= 1
                window_start += 1
            
            longest_length = max(longest_length, (window_end - window_start) + 1)
        
        return longest_length