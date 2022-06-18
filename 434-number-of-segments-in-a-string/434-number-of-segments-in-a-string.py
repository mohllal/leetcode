class Solution:
    # O(n) time and O(1) space
    def countSegments(self, s: str) -> int:
        count = 0
        
        for i in range(0, len(s)):
            if s[i] != ' ':
                if i == 0 or s[i - 1] == ' ':
                    count += 1
        return count