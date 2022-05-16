class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': (1, 0),
            'V': (5, 1),
            'X': (10, 2),
            'L': (50, 3),
            'C': (100, 4),
            'D': (500, 5),
            'M': (1000, 6),
        }
        
        result, lastIndex = roman[s[0]]
        
        for i in range(1, len(s)):
            val, index = roman[s[i]]
            if index <= lastIndex:
                result += val
            else:
                result -= roman[s[i-1]][0]
                result += val - roman[s[i-1]][0]
            lastIndex = index

        return result
                