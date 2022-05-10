class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        return result == result[::-1]