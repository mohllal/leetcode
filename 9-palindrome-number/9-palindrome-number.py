class Solution:
    # O(1) time and O(n) space
    def isPalindromeConstantTimeAndLinearSpace(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;
        
        xStr = str(x);
        xStrReversed = xStr[::-1];

        return xStr == xStrReversed;
    
    # O(n) time and O(1) space
    def isPalindromeLinearTimeAndConstantSpace(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False;

        lastHalfRevertedNumber = 0;

        while x > lastHalfRevertedNumber:
            lastHalfRevertedNumber = lastHalfRevertedNumber * 10 + (x % 10);
            x //= 10;

        return x == lastHalfRevertedNumber or x == lastHalfRevertedNumber//10;
    
    def isPalindrome(self, x: int) -> bool:
        return self.isPalindromeLinearTimeAndConstantSpace(x)