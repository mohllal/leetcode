from collections import defaultdict

class Solution:
    # O(n) time and O(n) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = list(s)
        repeats = defaultdict(lambda: 0)
        maxLength = 0

        start = 0
        end = 0
        while end < len(characters):
            repeats[characters[end]] += 1

            while len(repeats) < end - start + 1:
                repeats[characters[start]] -= 1
                if repeats[characters[start]] == 0:
                    del repeats[characters[start]]

                start += 1
            
            maxLength = max(maxLength, end - start + 1)
            end += 1

        return maxLength