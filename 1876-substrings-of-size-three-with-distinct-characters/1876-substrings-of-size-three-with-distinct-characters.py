from collections import defaultdict

class Solution:
    # O(n) time and O(n) space
    def countGoodSubstrings(self, s: str) -> int:
        characters = list(s)
        
        result = 0
        unique = defaultdict(lambda: 0)
        for i in range(0, len(characters)):
            unique[characters[i]] += 1
            
            if i >= 2:
                if (
                    unique[characters[i]] == 1
                    and unique[characters[i - 1]] == 1
                    and unique[characters[i - 1]] == 1
                ):
                    result += 1
    
                unique[characters[i - 2]] -= 1
        return result