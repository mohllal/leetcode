class Solution:
    # O(n) time and O(1) space
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0
        
        i = 1
        while i < len(arr) - 1:
            isPeak = arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
            
            if not isPeak:
                i += 1
                continue
            
            left = i - 2
            while left >= 0 and arr[left] < arr[left + 1]:
                left -= 1
            
            right = i + 2
            while right < len(arr) and arr[right] < arr[right - 1]:
                right += 1
            
            longest = max(longest, right - left - 1)
            i = right
        
        return longest