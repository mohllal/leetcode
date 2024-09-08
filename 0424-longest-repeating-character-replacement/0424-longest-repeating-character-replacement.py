from collections import Counter

class Solution:
    # O(n) time and O(1) space
    # O(26 * n) ~= O(n) time
    def characterReplacement1(self, s: str, k: int) -> int:
        longest_length = 0
        
        window_start = 0
        window_counter = Counter()
        for window_end in range(len(s)):
            window_end_letter = s[window_end]        
            window_counter[window_end_letter] += 1
    
            while (window_end - window_start + 1) - max(window_counter.values()) > k:
                window_start_letter = s[window_start]
                window_counter[window_start_letter] -= 1
                window_start += 1
            
            longest_length = max(longest_length, (window_end - window_start) + 1)
            
        return longest_length
    
    # O(n) time and O(1) space
    def characterReplacement2(self, s: str, k: int) -> int:
        longest_length = 0
        
        window_start = 0
        window_counter = Counter()
        max_letter_count = 0
        for window_end in range(len(s)):
            window_end_letter = s[window_end]
            window_counter[window_end_letter] += 1

            max_letter_count = max(max_letter_count, window_counter[window_end_letter])
    
            while (window_end - window_start + 1) - max_letter_count > k:
                window_start_letter = s[window_start]
                window_counter[window_start_letter] -= 1
                window_start += 1
            
            longest_length = max(longest_length, (window_end - window_start) + 1)
            
        return longest_length
    
    def characterReplacement(self, s: str, k: int) -> int:
        return self.characterReplacement2(s, k)