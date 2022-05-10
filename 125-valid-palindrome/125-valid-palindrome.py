class Solution:
    def isPalindromeNaive(self, s: str) -> bool:
        result = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        return result == result[::-1]

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        while i < len(s) and j >= 0:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True