from collections import Counter

class Solution:
    # O(n + m) time and O(n + m) space
    # where n is the length of 's' and m is the length of 't'
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        t_counter = Counter(t)
        
        window_start = 0
        window_matched_letters = 0
        for window_end in range(len(s)):
            window_end_letter = s[window_end]
            
            if window_end_letter in t_counter:
                t_counter[window_end_letter] -= 1

                if t_counter[window_end_letter] == 0:
                    window_matched_letters += 1
            
            while window_matched_letters == len(t_counter):
                candidate = s[window_start:window_end+1]
                if result == "" or len(candidate) < len(result):
                    result = candidate
                
                window_start_letter = s[window_start]
                if window_start_letter in t_counter:
                    if t_counter[window_start_letter] == 0:
                        window_matched_letters -= 1

                    t_counter[window_start_letter] += 1
                
                window_start += 1
        
        return result
                