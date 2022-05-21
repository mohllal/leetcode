class Solution:
    # O(n) time and O(n) space
    def isPalindromeLinearTimeAndLinearSpace(self, s: str) -> bool:
        result = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        return result == result[::-1]

    # O(n) time and O(1) space
    def isPalindromeLinearTimeAndConstantSpace(self, s: str) -> bool:
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

    def isPalindrome(self, s: str) -> bool:
        return self.isPalindromeLinearTimeAndConstantSpace(s)