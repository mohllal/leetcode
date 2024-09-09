from collections import Counter
import string

class Solution:
    # O(n + m) time and O(26) ~= O(1) space
    # where n is the length of s1 and m is the length of s2
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        # O(n) time and O(1) space
        s1_counter = Counter(s1)
        
        window_start = 0
        window_matched_letters = 0
        for window_end in range(len(s2)):
            window_end_letter = s2[window_end]
            
            # if the letter is part of s1, decrease its frequency in the counter
            if window_end_letter in s1_counter:
                s1_counter[window_end_letter] -= 1
                
                # if the frequency becomes zero, it means we have matched all instances of this letter
                if s1_counter[window_end_letter] == 0:
                    window_matched_letters += 1
            
            # if all letters from s1 are matched, return True
            if window_matched_letters == len(s1_counter):
                return True
    
            # shrink the window
            if window_end >= len(s1) - 1:
                window_start_letter = s2[window_start]
        
                # if the letter that is leaving is part of s1, increment its frequency back in the counter
                if window_start_letter in s1_counter:
                    # if this letter was previously fully matched, we lose the match for it
                    if s1_counter[window_start_letter] == 0:
                        window_matched_letters -= 1
                    s1_counter[window_start_letter] += 1
                
                window_start += 1
        
        return False
    
    # O(n + (26 * m)) ~= O(n + m) time and O(1) space
    # where n is the length of s1 and m is the length of s2
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1_counter = Counter({char: 0 for char in string.ascii_lowercase})
        s2_counter = Counter({char: 0 for char in string.ascii_lowercase})
        
        # O(n) time and O(1) space
        s1_counter.update(s1)
        
        window_start = 0
        for window_end in range(len(s2)):
            window_end_letter = s2[window_end]
            s2_counter[window_end_letter] += 1
            
            if window_end >= len(s1) - 1:
                # O(26) ~= O(1) time and O(1) space
                if s1_counter == s2_counter:
                    return True
    
                window_start_letter = s2[window_start]
                s2_counter[window_start_letter] -= 1
                window_start += 1
    
        return False 
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.checkInclusion2(s1, s2)