from collections import Counter

class Solution:
    # O(n + m) time and O(26) ~= O(1) space
    # where n is the length of the 's' string and m is the length of the 'p' string
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagrams = []

        # O(m) time and O(1) space
        p_counter = Counter(p)

        window_start = 0
        window_matched_letters = 0
        for window_end in range(len(s)):
            window_end_letter = s[window_end]
            
            # if the letter is part of p, decrease its frequency in the counter
            if window_end_letter in p_counter:
                p_counter[window_end_letter] -= 1
    
                # if the frequency becomes zero, it means we have matched all instances of this letter
                if p_counter[window_end_letter] == 0:
                    window_matched_letters += 1
            
            # if all letters from p are matched, save window start
            if window_matched_letters == len(p_counter):
                anagrams.append(window_start)
            
            # shrink the window when its length is longer than the pattern length
            if window_end >= len(p) - 1:
                window_start_letter = s[window_start]
                
                # if the letter that is leaving is part of s1, increment its frequency back in the counter
                if window_start_letter in p_counter:
                    # if the letter was previously fully matched, we lose the match for it
                    if p_counter[window_start_letter] == 0:
                        window_matched_letters -= 1
    
                    p_counter[window_start_letter] += 1

                window_start += 1

        return anagrams